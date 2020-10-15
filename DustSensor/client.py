 # -*- coding: utf-8 -*-
 # author : http://github.com/jeonghoonkang
 # author : http://github.com/sonnonet
from socket import *
from select import *
import time
import influx_simple_driver
import requests, json
from influxdb import InfluxDBClient as influxdb

HOST = '192.168.0.7'
PORT = 9999
ADDR = (HOST,PORT)
client_socket = socket(AF_INET,SOCK_STREAM)

client_socket.connect(ADDR)

if __name__=="__main__" :

    try:
        print("Starting")
        #hpma115S0 = HPMA115S0.HPMA115S0("/dev/ttyAMA0")
        hpma115S0 = HPMA115S0.HPMA115S0("/dev/serial0")

        hpma115S0.init()
        hpma115S0.startParticleMeasurement()

        client=influxdb('localhost',8086,'root','root','example_script')

# 키보드로 입력한 문자열을 서버로 전송하고 

# 서버에서 에코되어 돌아오는 메시지를 받으면 화면에 출력합니다. 

# quit를 입력할 때 까지 반복합니다. 
        while True:
            if (hpma115S0.readParticleMeasurement()):
                print("PM2.5: %d ug/m3" % (hpma115S0._pm2_5))
                print("PM10: %d ug/m3" % (hpma115S0._pm10))
                pm2 = hpma115S0._pm2_5
                pm10 = hpma115S0._pm10
                clientSocket.send(pm2.encode())
                clientSocket.send(pm10.encode())
# if ret != True : print "[problem|influx]"
            time.sleep(3)


    except KeyboardInterrupt:
        print("program stopped")


client_socket.close()

