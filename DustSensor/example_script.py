# -*- coding: utf-8 -*-
# author : http://github.com/jeonghoonkang
# author : http://github.com/sonnonet

import HPMA115S0
import time
import influx_simple_driver
import requests, json
from influxdb import InfluxDBClient as influxdb

if __name__=="__main__" :

    try:
        print("Starting")
        #hpma115S0 = HPMA115S0.HPMA115S0("/dev/ttyAMA0")
        hpma115S0 = HPMA115S0.HPMA115S0("/dev/serial0")
        '''라즈베리파이 스트레치 부터는 기존 AMA0 은 BLE로 사용하면서, 디바이스 파일 명칭 바뀜'''
        hpma115S0.init()
        hpma115S0.startParticleMeasurement()

#        client=influxdb('localhost',8086,'root','root','example_script')


        while True:
            if (hpma115S0.readParticleMeasurement()):
                print("PM2.5: %d ug/m3" % (hpma115S0._pm2_5))
                print("PM10: %d ug/m3" % (hpma115S0._pm10))
               # ret = influx_simple_driver.influx_write(hpma115S0._pm2_5, '210.125.198.85')
               # if ret != True : print "[problem|influx]"
            time.sleep(4)


    except KeyboardInterrupt:
        print("program stopped")
