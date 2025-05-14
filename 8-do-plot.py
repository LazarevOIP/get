import numpy as np
import matplotlib.pyplot as plt
import textwrap

with open('data.txt', 'r') as f:
    adc_data = np.array([int(line.strip()) for line in f.readlines()])
with open('settings.txt', 'r') as f:
    settings = [float(line.strip()) for line in f.readlines()]
    
time_step = settings[0]     # шаг по времени в секундах
voltage_step = settings[1]  # шаг по напряжению в Вольтах

voltages = adc_data * voltage_step
time = np.arange(len(adc_data)) * time_step

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(time, voltages, label="V(t)",
        color='blue', linestyle='-', linewidth=2,
        marker='o', markersize=4, markerfacecolor='red',
        markeredgecolor='black', markevery=10)              #markevery do only 10ths markers

ax.set_xlim(np.min(time), np.max(time))
ax.set_ylim(np.min(voltages)-0.1, np.max(voltages)+0.1)
ax.set_xlabel("Время, с", fontsize=12)
ax.set_ylabel("Напряжение, В", fontsize=12)

title_text = ("График зависимости напряжения на конденсаторе "
              "от времени в RC-цепи при зарядке и разрядке")
wrapped_title = "\n".join(textwrap.wrap(title_text, width=50))
ax.set_title(wrapped_title, loc='center', wrap=True)

ax.grid(which='major', color='gray', linestyle='--', linewidth=0.5)
ax.minorticks_on()
ax.grid(which='minor', color='lightgray', linestyle=':', linewidth=0.5)

ax.legend(loc='best')

max_index = np.argmax(voltages)
charge_time = time[max_index]
discharge_time = time[-1] - time[max_index]

text_x = np.mean(time)*1.5
text_y = np.max(voltages) * 0.5

text = (f"Время зарядки: {charge_time:.2f} с\n"
        f"Время разрядки: {discharge_time:.2f} с")

ax.text(text_x, text_y, text, fontsize=10, color='darkgreen',
        bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round,pad=0.5'),
        ha='center')

plt.tight_layout()
plt.savefig("Lesson8-rc-results.svg", format='svg')
plt.show()