import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # Verwendet die BCM-Pinnummerierung
GPIO.setup(18, GPIO.OUT)  # Pin 18 als Ausgang setzen
GPIO.setup(23, GPIO.OUT)  
#while True:
GPIO.output(23, GPIO.LOW)  # 23 --> GPIO 0 --> Flash Mode
time.sleep(1)  # 1 Sekunde warten
GPIO.output(18, GPIO.LOW)  # Pin 18 low --> reset
time.sleep(1)  # 1 Sekunde warten
GPIO.output(18, GPIO.HIGH) 
