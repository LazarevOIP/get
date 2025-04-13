import RPI.GPIO as GPIO #Библиотека портов ввода вывода 
import time #Библиотека time

GPIO.setmode(GPIO.BCM)

GPIO.setup(2,GPIO.IN)
GPIO.setup(3,GPIO.IN)

for i in range (10):
    GPIO.output(3,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(3,GPIO.LOW)
    time.sleep(1)