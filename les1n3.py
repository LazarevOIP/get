import RPI.GPIO as GPIO #Библиотека портов ввода вывода 
import time #Библиотека time

GPIO.setmode(GPIO.BCM)

GPIO.setup(2,GPIO.IN)
GPIO.setup(3,GPIO.IN)

GPIO.output(3,GPIO.input(2))
time.sleep(5)