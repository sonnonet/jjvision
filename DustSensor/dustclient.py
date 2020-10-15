# -*- coding: utf-8 -*-
import socket
from threading import Thread
import HPMA115S0
import time
import influx_simple_driver
import requests, json
from influxdb import InfluxDBClient as influxdb


host = "192.168.0.7"
port = 3334

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host,port))


if __name__=="__main__" :

	try:
		print("Starting")
		#hpma115S0 = HPMA115S0.HPMA115S0("/dev/ttyAMA0")
		hpma115S0 = HPMA115S0.HPMA115S0("/dev/serial0")

		hpma115S0.init()
		hpma115S0.startParticleMeasurement()
		client=influxdb('localhost',8086,'root','root','example_script')



		while True:
			if (hpma115S0.readParticleMeasurement()):
				print("PM2.5: %d ug/m3" % (hpma115S0._pm2_5))
				print("PM10: %d ug/m3" % (hpma115S0._pm10))
				data ="Sensor B " + str(hpma115S0._pm2_5)+ " " + str(hpma115S0._pm10)
				sock.send(data.encode())
				# ret = influx_simple_driver.influx_write(hpma115S0._pm2_5, '    210.125.198.85')
				# if ret != True : print "[problem|influx]"
 			time.sleep(4)



                sock.close()

	except KeyboardInterrupt:
		print("program stopped")
