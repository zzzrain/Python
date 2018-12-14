#!usr/bin/evn python
# coding=utf-8

import requests

resGZ = requests.get('http://wthrcdn.etouch.cn/weather_mini?city='+'广州')
dataGZ = resGZ.json()['data']['forecast'][0]

print resGZ.json()['data']['city'], dataGZ['date'], dataGZ['high'], dataGZ['low'], dataGZ['type']

for key in ['广州', '北京', '上海']:
    res = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + key)
    data = res.json()['data']['forecast'][0]
    print res.json()['data']['city'], data['date'], data['high'], data['low'], data['type']
