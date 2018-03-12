import serial
import numpy

tempF = []

arduinoData = serial.Serial('COM3', 9600)

while True :
    while (arduinoData.inWaiting()==0):
        pass
    arduinoString = arduinoData.readline()
    dataArray = arduinoString.split()
    temp = float(dataArray[0])
    tempF.append(temp)
    print(tempF)
    
