#!/usr/bin/env python3

#from __future__ import print_funtion

import ex1_kwstest as kws
import ex2_getVoice2Text as gv2t
import ex4_getText2VoiceStream as tts
import Adafruit_DHT as dht
import time
import MicrophoneStream as MS
import RPi.GPIO as GPIO

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17,GPIO.HIGH)
time.sleep(1)
GPIO.output(17,GPIO.LOW)


def checkCommand(result):
    h,t = dht.read_retry(11,4)
    text = result
    if text.find("온도") >=0:
        print("현재온도 {} 도 입니다 ".format(t))
        if t >=26:
            GPIO.output(17, GPIO.HIGH)
        return("현재 온도 {} 도 입니다 적정온도 26도 이상이면 불이 켜집니다 ".format(t))

    elif text.find("습도") >= 0:
        print("현재습도 {} 퍼센트 입니다 ".format(h))
        if h >=50:
            GPIO.output(17, GPIO.HIGH)
        return("현재습도 {} 퍼센트 입니다 적정습도 50퍼센트 이상이면 불이 켜집니다".format(h))

    elif text.find("켜") >= 0:
        print("불이 켜집니다.")
        GPIO.output(17, GPIO.HIGH)
        return("불이 켜집니다")
    
    elif text.find("커") >= 0:
        print("불이 켜집니다.")
        GPIO.output(17, GPIO.HIGH)
        return("불이 켜집니다")

    elif text.find("꺼") >= 0:
        print("불이 꺼집니다.")
        GPIO.output(17, GPIO.LOW)
        return("불이 꺼집니다.")
    
    elif text.find("꺽") >= 0:
        print("불이 꺼집니다.")
        GPIO.output(17, GPIO.LOW)
        return("불이 꺼집니다.")

    else:
        return("죄송합니다, 이해하지 못했습니다")

def main():
    KWSID = ['친구야']
    while 1:
        recog=kws.test(KWSID[0])
        if recog == 200:
            print('kws Dectected ..\n Start STT...')
            text = gv2t.getVoice2Text()
            print('Recognized Text: ' + text)
            tts.getText2VoiceStream(checkCommand(text), "result_TTS.wav")
            MS.play_file("result_TTS.wav")
            time.sleep(1)
        else:
            print('KWS Not Dectected _')
if __name__ == '__main__':
    main()

