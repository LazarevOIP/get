import RPi.GPIO as GPIO

dac = [8,11,7,1,0,5,12,6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def Dec_to_bin_func (dec):
    return list(map(int, "{0:08b}".format(dec)))

try:
    while (True):
        user_in = input("Введите dec(0-255): ")
        try:
            num = float(user_in)
            if num.is_integer():
                user_in = int(user_in)
                if 0 <= user_in <= 255:
                    GPIO.output(dac, Dec_to_bin_func(user_in))
                    voltage_output = float(user_in)/256 *3.3
                    print (round(voltage_output,5), "В выходное напряжение")   
                else:
                    if user_in < 0:
                       print("Ваше число отрицательное!")
                    elif user_in > 0:
                        print("Ваше число превышающет возможности 8-разрядного ЦАП!")
            else:
                print("Вы ввели не целое число от 0 до 255!")
        except Exception:
            if user_in == "q":
                break 
            print("Вы ввели строку!") 

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()