
from gpiozero import CPUTemperature

def getTemperature():
    cpu = CPUTemperature()
    return cpu.temperature
