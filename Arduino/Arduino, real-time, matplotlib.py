import serial
import numpy
import matplotlib.pyplot as plt
from drawnow import *

tempF = []
arduinoData = serial.Serial('COM3', 9600)
plt.ion()

def makeFig() :
    plt.plot(tempF, 'ro-')


while True :
    while (arduinoData.inWaiting()==0):
        pass
    arduinoString = arduinoData.readline()
    dataArray = arduinoString.split()
    temp = float(dataArray[0])
    tempF.append(temp)
    drawnow(makeFig)
    
