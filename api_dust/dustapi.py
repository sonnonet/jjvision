#-*-coding: utf-8 -*-

import requests, xmltodict, json
from bs4 import BeautifulSoup
import pandas as pd

ver ='&ver=1.3'
stat="stationName="+"팔복동"+"&dataTerm=month&pageNo=1&numOfRows=100&ServiceKey="
key ='n418NRGApmI4sI2piGtO98z2yNQ6lWeaHqvuyd3MoKoCZGO6WMblMSmiWBZV3XnJ8TGbX9oDOI0mkAZtTRLSPg%3D%3D'
url ='http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?'+stat+key+ver
print(url)
response = requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")

ItemList = soup.findAll('item')

for item in ItemList:
#	print('아오')
	a = item.find('datatime').text
	g = item.find("pm10value").text
	i = item.find("pm25value").text
	s = item.find("pm10grade1h").text
	t = item.find("pm25grade1h").text

	print('측정소:팔복동')
	print('측정시간:' + a)
	print('미세먼지 농도:' +g+'ug/m3('+s+')')


