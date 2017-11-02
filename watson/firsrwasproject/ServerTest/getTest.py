# import http.client
# # print("/putdatatest?userName=myUN&pass=mypass&dID=202&temp=25&humi=50%")
# conn = http.client.HTTPSConnection("ubuntuteng", 8000)
# conn.request("GET", "/putdatatest?userName=myUN&pass=mypass&dID=202&temp=25&humi=50%")

# r1 = conn.getresponse()
# while not r1.closed:
#     print(r1.read(200))

# import http.client
# conn = http.client.HTTPSConnection("192.168.1.108",8000)
# conn.request("GET", "/test")
# r1 = conn.getresponse()
# print(res.status, r1.reason)

# import urllib2
# httpfeedback=urllib2.urlopen("http://ubuntuteng:8000/test").read()
# print(httpfeedback)



# import urllib.request
# with urllib.request.urlopen('http://ubuntuteng:8000/test') as response:
#    html = response.read()



import urllib.request
url='http://ubuntuteng:8000/'
indexTest='test'
showDatatest='showDatatest?userName=lwq&pass=pass'
putDatatest='putdatatest?userName=myUN&pass=mypass&dID=202&temp=25&humi=50%'
logintest='logintest'
Signuptest='signUptest?userName=testusername&pass=testpassword&userNicname=testnickname&email=testemail&userAge=testage&rheumatoidAge=testrage&city=testcit&dName=testdname&dID=testdid&dd=testdd'


suffixList=[indexTest,showDatatest,putDatatest,logintest,Signuptest]
for suffixurl in suffixList:
    req = urllib.request.Request(url+suffixurl)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page)
        print('\n')
        print('OK')
        print('\n')

