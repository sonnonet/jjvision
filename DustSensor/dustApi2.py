import requests

from bs4 import BeautifulSoup

import pandas

M = '&numOfRows=1&pageNo=1&stationName=&dataTerm=DAILY&ver=1.3'

key = 'qlfzz2TbihUtSfuoSHWkZXvBvZYgh402FIBNSRucaRCp64qcj4Pd4%2BrIETuwNUpWsCGVKESAVOVg7EtC3iIouw%3D%3D'

url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey='+ key + M

 

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

ItemList = soup.findAll('item')

for item in ItemList:

    a = item.find('datatime').text

    g = item.find('pm10value').text

    i = item.find('pm25value').text

    s = item.find('pm10grade1h').text

    t = item.find('pm25grade1h').text

    print('M')


