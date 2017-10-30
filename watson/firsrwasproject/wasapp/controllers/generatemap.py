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
    