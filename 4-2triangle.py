import RPi.GPIO as GPIO
import time

dac = [8,11,7,1,0,5,12,6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def Dec_to_bin_func (dec):
    return list(map(int, "{0:08b}".format(dec)))
try:
    try:
        period = input("Введите период: ")
        period = float(period)
        periodtime = period/512 
        t = 0 
        pm = 0
        while (True):
            t = t % 256
            GPIO.output(dac, Dec_to_bin_func(t))
            time.sleep(periodtime)
            if pm == 0:
                t = t + 1
            else:
                t = t - 1
            if t == 255:
                pm = 1
            if t == 0:
                pm = 0
    except Exception:
        print("Введите верное значение периода")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()