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
    for result in range(256):
        GPIO.output(dac, Dec_to_bin_func(result))
        res_comp = GPIO.input(comp)
        time.sleep(0.01)
        if res_comp:
            return result
    return 0

try:
    while True:
        time_start = time.time()
        res_adc = adc()
        time_end = time.time()
        voltage_adc = res_adc*3.3/256
        print("Voltage:",round(voltage_adc,4), "Time Adc:", round(time_end-time_start, 3))
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()