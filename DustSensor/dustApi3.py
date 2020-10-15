#-*-coding:utf-8-*-

from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus,unquote
import xml.etree.ElementTree as ET

txt_Output = False 
cmd_Output = True

#File Set
if txt_Output == True :
    Out_file = open("Output.txt", 'w')
    Out_file.write(u"Write Start\n")
    Out_file.close()

#API Set 1
API_key = unquote('qlfzz2TbihUtSfuoSHWkZXvBvZYgh402FIBNSRucaRCp64qcj4Pd4%2BrIETuwNUpWsCGVKESAVOVg7EtC3iIouw%3D%3D')
url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : API_key, quote_plus('numOfRows') : '10', quote_plus('pageNo') : '1', quote_plus('itemCode') : 'PM10', quote_plus('dataGubun') : 'HOUR', quote_plus('searchCondition') : 'MONTH' })

#API Call(For dustcheck)
request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read().decode('utf-8')
root = ET.fromstring(response_body)


def Read(): #API Read
    request = Request(url + queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('utf-8')
    root = ET.fromstring(response_body)

def dustcheck(city): #Search
    Read() #API Read
    dustinfo = root.find('body').find('items').find('item').find(city)
    if txt_Output == True :
        Out_file = open("Output.txt", 'a')
        Out_file.write(city + u"\n" + dustinfo.text)
    if cmd_Output == True :
        print(city + ' : ' + dustinfo.text + u' ug/m3')

    if 0 < int(dustinfo.text) <= 30: #좋음
        if cmd_Output == True :
            print(city + u" : 좋음\n")
        if txt_Output == True :
            Out_file.write(u" -> Good\n")
    elif 30 < int(dustinfo.text) <= 80:  #보통
        if cmd_Output == True :
            print(city + u" : 보통\n")
        if txt_Output == True :
            Out_file.write(u" -> Nomal\n")
    elif 80 < int(dustinfo.text) <= 150:  #나쁨
        if cmd_Output == True :
            print(city + u" : 나쁨\n")
        if txt_Output == True :
            Out_file.write(u" -> Bad\n")
    elif 150 < int(dustinfo.text):  #매우 나쁨
        if cmd_Output == True :
            print(city + u" : 매우 나쁨\n")
        if txt_Output == True :
            Out_file.write(u" -> Very Bad\n")

    if txt_Output == True :
        Out_file.close()

if __name__ == "__main__":
    dustcheck('seoul')
    dustcheck('busan')
