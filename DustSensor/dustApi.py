import json
import requests

your_province = ''
gov_api_key = 'qlfzz2TbihUtSfuoSHWkZXvBvZYgh402FIBNSRucaRCp64qcj4Pd4%2BrIETuwNUpWsCGVKESAVOVg7EtC3iIouw%3D%3D'
microdust_req_url = 'http://openapi.airkorea.or.kr/openapi/services/rest/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo?serviceKey=%s&pageNo=1&numOfRows10&year=2020&itemCode=&' % (gov_api_key)

dustdatatext = requests.get(microdust_req_url).text
dust_data = json.loads(dustdatatext)
my_city_data = dust_data['list'][0]
pm10 = my_city_data['pm10Value']
pm25 = my_city_data['pm25Value']

print(pm10)
print(pm25)

