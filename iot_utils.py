
import time
from gpiozero import CPUTemperature



def getTemperature():
    cpu = CPUTemperature()
    return cpu.temperature


if __name__ == '__manin__':
    print("CPU Temp: ", getTemperature()," °C")
    time.sleep(2.5)
