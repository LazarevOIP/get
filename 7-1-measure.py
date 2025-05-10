#Импорт требуемых библиотек
import RPi.GPIO as GPIO
import matplotlib.pyplot as plot
import time

#Обьявление переменных
dac = [8,11,7,1,0,5,12,6]
led = [2,3,4,17,27,22,10,9]
comp = 14
troyka = 13

#Назначение пинов
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(comp, GPIO.IN)

#Функция перевода десятичного в бинарный
def Dec_to_bin_func (dec):
    return [int(element) for element in bin(dec)[2:].zfill(8)]

#Функция компаратор выявляет значение 0-255
def adc():
    result = 0

    result += 128
    GPIO.output(dac, Dec_to_bin_func(result))
    time.sleep(0.004)
    if  GPIO.input(comp):
        result -= 64 
    else:
        result += 64
    
    GPIO.output(dac, Dec_to_bin_func(result))
    time.sleep(0.004)
    if  GPIO.input(comp):
        result -= 32
    else:
        result += 32
    
    GPIO.output(dac, Dec_to_bin_func(result))
    time.sleep(0.004)
    if  GPIO.input(comp):
        result -= 16
    else:
        result += 16

    GPIO.output(dac, Dec_to_bin_func(result))
    time.sleep(0.004)
    if  GPIO.input(comp):
        result -= 8
    else:
        result += 8

    GPIO.output(dac, Dec_to_bin_func(result))
    time.sleep(0.004)
    if  GPIO.input(comp):
        result -= 4
    else:
        result += 4

    GPIO.output(dac, Dec_to_bin_func(result))
    time.sleep(0.004)
    if  GPIO.input(comp):
        result -= 2
    else:
        result += 2

    GPIO.output(dac, Dec_to_bin_func(result))
    time.sleep(0.004)
    if  GPIO.input(comp):
        result -= 1
    else:
        result += 1

    GPIO.output(dac, Dec_to_bin_func(result))
    time.sleep(0.004)
    if  GPIO.input(comp):
        result -= 1
        GPIO.output(dac, Dec_to_bin_func(result))

    return result

#Функция вывыода значения в dac
def Dac_Out_Func(dec):
    array_out = Dec_to_bin_func(dec)
    GPIO.output(dac, array_out)
    return array_out

GPIO.output(troyka, 0)

array_voltages_data = []
array_times_data = []

try:
    time_start = time.time()
    res_adc = 0
    GPIO.output(troyka, 1)
    
    #Цикл зарядки конденсатора и записи данных
    while (res_adc < 206):
        res_adc = adc()
        Dac_Out_Func(res_adc)
        #time_end = time.time()
        #voltage_adc = res_adc*3.3/255
        #print("Voltage:",round(voltage_adc,4), "Time Adc:", round(time_end-time_start, 6))
        #array_voltages_data.append(voltage_adc)
        #array_times_data.append(time_end-time_start)
        array_voltages_data.append(res_adc)
        array_times_data.append(time.time())

    GPIO.output(troyka, 0)

    #Цикл разрядки конденсатора и записи данных
    while (res_adc > 180):#16
        res_adc = adc()
        Dac_Out_Func(res_adc)
        #time_end = time.time()
        #voltage_adc = res_adc*3.3/255
        #print("Voltage:",round(voltage_adc,4), "Time Adc:", round(time_end-time_start, 6))
        #array_voltages_data.append(voltage_adc)
        #array_times_data.append(time_end-time_start)
        array_voltages_data.append(res_adc)
        array_times_data.append(time.time())

    time_end = time.time()

    #Запись данных в файл
    quant_step = 3.3 / 255
    avg_time = (time_end - time_start) / len(array_times_data)
    freq = 1 / avg_time
    with open("settings.txt", 'w') as file:
        file.write(f"{freq}\n")         # частота дискретизации
        file.write(f"{quant_step}\n")   # шаг квантования

    print("Time all experiment:  ", round(time_end - time_start, 6))
    print("Period one measurement:", round((time_end - time_start) / len(array_times_data), 6))
    print("Quantization step:     ", round(quant_step,6))
    print("Frequance:            ", round(freq,6))

    sum_time = 0
    for i in range(len(array_times_data)-1):
        sum_time =+ (array_times_data[i+1] - array_times_data[i]) 
    freq2 = len(array_times_data)/sum_time
    print("Frequance:",round(freq2,6)) #Чистатя чистота измерений без учета лишних действий

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()

strs_voltages_data = [str(i) for i in array_voltages_data]
strs_time_data = [str(i) for i in array_times_data]

#Запись данных в файл
with open("data.txt", 'w') as file:
    file.write('\n'.join(strs_voltages_data))
    file.close()

#Построение графика на основе полученных данных
plot.plot(array_times_data, array_voltages_data)
plot.show()