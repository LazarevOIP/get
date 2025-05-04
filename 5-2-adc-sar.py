import RPi.GPIO as GPIO
import time

dac = [8,11,7,1,0,5,12,6]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT,initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def Dec_to_bin_func (dec):
    return [int(element) for element in bin(dec)[2:].zfill(8)]

def adc():
    result = 0

    result += 128
    GPIO.output(dac, Dec_to_bin_func(result))
    time.sleep(0.01)
    if  GPIO.input(comp):
        result -= 64 
    else:
        result += 64
    
    GPIO.output(dac, Dec_to_bin_func(result))
    time.sleep(0.01)
    if  GPIO.input(comp):
        result -= 32
    else:
        result += 32
    
    GPIO.output(dac, Dec_to_bin_func(result))
    time.sleep(0.01)
    if  GPIO.input(comp):
        result -= 16
    else:
        result += 16

    GPIO.output(dac, Dec_to_bin_func(result))
    time.sleep(0.01)
    if  GPIO.input(comp):
        result -= 8
    else:
        result += 8

    GPIO.output(dac, Dec_to_bin_func(result))
    time.sleep(0.01)
    if  GPIO.input(comp):
        result -= 4
    else:
        result += 4

    GPIO.output(dac, Dec_to_bin_func(result))
    time.sleep(0.01)
    if  GPIO.input(comp):
        result -= 2
    else:
        result += 2

    GPIO.output(dac, Dec_to_bin_func(result))
    time.sleep(0.01)
    if  GPIO.input(comp):
        result -= 1
    else:
        result += 1

    GPIO.output(dac, Dec_to_bin_func(result))
    time.sleep(0.01)
    if  GPIO.input(comp):
        result -= 1
        GPIO.output(dac, Dec_to_bin_func(result))

    return result

try:
    while True:
        time_start = time.time()
        res_adc = adc()
        time_end = time.time()
        voltage_adc = res_adc*3.3/256
        print("Voltage:",round(voltage_adc,4), "Time Adc:", round(time_end-time_start, 6))
        #time.sleep(1)
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()