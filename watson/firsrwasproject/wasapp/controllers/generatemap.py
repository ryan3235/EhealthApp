# -*- coding: utf-8 -*-
from watson import framework
from watson.framework import controllers
import http.client
import smtplib
from email.mime.text import MIMEText
import json
import threading
from wasapp.db import sqliteDB

class Generatemap(controllers.Rest):

    #temp limits
    tempLowLimit = 59;
    tempHighLimit = 70;

    #list of city in sdeney
    citysName = ['Badgerys%20Creek', 'Bankstown', 'Blacktown', 'Bondi', 'Camden', 'Campbelltown', 'Canterbury',
                 'Eastwood', 'Holsworthy', 'Homebush', 'Lane%20Cove', 'Liverpool', 'Mascot', 'Parramatta', 'Penrith',
                 'Prospect', 'Richmond', 'Sydney', 'Terrey%20Hills'];
    cityWeather = {};

    #email info
    mail_host = "smtp.163.com"
    mail_user = "cgrslwq"
    mail_pass = "lwq175606"
    mail_postfix1 = "163.com"

    def GET(self):
        threads = [];
        for city in self.citysName:
            thread = threading.Thread(target=self.httpGet(city));
            threads.append(thread);
            thread.start();
        for thread in threads:
            thread.join();

        sql='SELECT email,city FROM user'
        print(sql)
        result=sqliteDB().query(sql)
        result=result.fetchall()
        toList = [];
        for dinfor in result:
            city = dinfor[1]
            email = dinfor[0]
            if self.cityWeather[city]:
                print(city)
                toList.append(email)

        # toList = ['liuwenqing123@yahoo.com'];
        self.send_mail(toList,'test','hello wenqing');
        return {'weatherInfo':json.dumps(self.cityWeather)};

    #获取各城市的雅虎天气，试用多线程执行
    def httpGet(self,cityName):
        #雅虎天气获取的url
        baseUrl = 'query.yahooapis.com'
        # cityName1 = cityName
        # if cityName.__eq__('Badgerys Creek'):
        #     cityName1 = 'Badgerys%20Creek'
        # if cityName.__eq__()
        url =  '/v1/public/yql?format=json&q=select%20item.condition%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text=%22' + cityName +'%22)';

        conn = http.client.HTTPSConnection(baseUrl)
        conn.request(method="GET", url=url)

        response = conn.getresponse()
        res = response.read()
        # print(res);
        weather = {}
        if(res != b''):
            weather = json.loads(res.decode('utf8'))
        else:
            print("city is" + cityName)
        temp = 0;

        #acquire temp
        if (weather):
            if (weather['query']):
                temp = int(weather['query']['results']['channel']['item']['condition']['temp']);

        #there is a issue that i can not get the correct result from yahoo weather only i use 'Badgerys%20Creek' instead of 'Badgerys Creek'
        if (temp < self.tempLowLimit | temp > self.tempHighLimit):
            if cityName.__eq__('Badgerys%20Creek'):
                self.cityWeather['Badgerys Creek'] = temp
            elif cityName.__eq__('Terrey%20Hills'):
                self.cityWeather['Terrey Hills'] = temp
            elif cityName.__eq__('Lane%20Cove'):
                self.cityWeather['Lane Cove'] = temp
            else:
                self.cityWeather[cityName] = temp;


    def send_mail(self, to_list, sub, context):

        me = self.mail_user + "<" + self.mail_user + "@" + self.mail_postfix1 + ">"
        msg = MIMEText(context)
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = ";".join(to_list)
        try:
            send_smtp = smtplib.SMTP()
            send_smtp.connect(self.mail_host)
            # send_smtp.esmtp_features["auth"]="LOGIN PLAIN"
            send_smtp.login(self.mail_user, self.mail_pass)
            send_smtp.sendmail(me, to_list, msg.as_string())
            send_smtp.quit()
            return True
        except Exception as e:
            print(str(e))
            return False


