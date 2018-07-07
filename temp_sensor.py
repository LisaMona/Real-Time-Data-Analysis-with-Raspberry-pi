from gpiozero import CPUTemperature
from time import sleep, strftime, time
import matplotlib.pyplot as plt
import numpy as np

cpu = CPUTemperature()

plt.ion()
x = np.zeros(20)
y = np.zeros(20)
x = x.tolist()
y = y.tolist()

def write_temp(temp):
    with open("/home/pi/Documents/cpu_temp.csv", "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))
    
def graph(temp):
    
    plt.clf()
    plt.scatter(x,y)
    plt.plot(x,y)
    plt.show()
    plt.pause(0.01)

while True:
    temp = cpu.temperature
    write_temp(temp)
    y.append(temp)
    x.append(time())
    x = x[-20:]
    y = y[-20:]
    if y[-1] > 60:
        print("Alert")
        print(y[-1])
    else:
        print("OK")   
    graph(temp)
   
