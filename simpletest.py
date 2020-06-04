#!/usr/bin/python

import Adafruit_DHT
import time
import requests, json
from influxdb import InfluxDBClient as influxdb

sensor = Adafruit_DHT.DHT11

pin = '4'

try:
    while True:
        h,t = Adafruit_DHT.read_retry(sensor, pin)
        if h is not None and t is not None:
            data = [{
                'measurement' : 'th',
                'tags':{
                    'office': '1',
                },
                'fields':{
                    'temp' : t,
                    'humi' : h,
                }
            }]
            
            print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(t,h))
        else:
            print("Read error")
        client = None
        try:
            client = influxdb('localhost',8086,'root','root','jjvision')
        except Exception as e:
            print "Exception" + str(e)
        if client is not None:
            try:
                client.write_points(data)
            except Exception as e:
                print "Exception write" + str(e)
            finally:
                client.close()
        
        time.sleep(1)
except KeyboardInterrupt:
    print("Terminated by Keyboard")

finally:
    print("End of Program")

