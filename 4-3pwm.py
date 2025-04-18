import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

pwm_output = GPIO.PWM(21,1000)
pwm_output.start(0)

try:
    while (True):
        coff = int(input("Введите коэф.: "))
        pwm_output.ChangeDutyCycle(coff)
        print(3.3*coff/100)
finally:
    pwm_output.stop()
    GPIO.output(21, 0)
    GPIO.cleanup()