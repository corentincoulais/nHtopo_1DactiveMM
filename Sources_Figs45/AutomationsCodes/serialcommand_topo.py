__linux_serialdeviceCmd__ = "/dev/ttyACM0"
__win_serialdeviceCmd__ = "COM5"

import time
import sys, os
import serial
import csv
import re
import numpy as np
import pulseSniffer_Adriaan as sData

def initSerialDevices():
    global serCmd, serData

    if os.name=="posix":
        serCmd = serial.Serial(__linux_serialdeviceCmd__, 115200, timeout=2.0)
        print("serial device %s initialized"%__linux_serialdeviceCmd__)
    else:    
        serCmd = serial.Serial(__win_serialdeviceCmd__, 115200, timeout=2.0)
        print("serial device %s initialized"%__win_serialdeviceCmd__)

def sendCmd(cmdstr):
    global serCmd
    print("sending: ",cmdstr)
    serCmd.write(cmdstr+"\r\n".encode('utf-8'))
    serCmd.flush()

def print_menu():
    print("commands:")
    print("f <value> - set frequency in Hz. Example f 0.5")
    print("a <value> - set amplitude. Example a 200")
    print("x - stop motor")
    print("s - start motor")
    c = str( input("cmd>")).encode ('utf-8')
    return c


def commandMain(amplitude, freq, collectionTime):
    amplitudeSet = ("a " + str(amplitude)).encode ('utf-8')
    startCommand = "s".encode ('utf-8')
    stopCommand = "x".encode ('utf-8')
    
    sendCmd(amplitudeSet)
    time.sleep(0.5)
    
    # Set frequency for this measurement.
    frequencySet = ("f " + str(freq)).encode ('utf-8')
    sendCmd(frequencySet)
    time.sleep(0.5)
    
    # Determine fileName based on input frequency
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    dumpPath = os.path.join(fileDir, 'captureDump/')
    fileIndex = len(os.listdir(dumpPath)) + 1
    fileName = "10pendulanAngles" + str(fileIndex) +'-'+ str(freq)+'-'+str(amplitude)+'-'+str(collectionTime)+'-'+'0fb'+ ".txt"
    # Initialise the data collection arduinoes.
    sData.initSerialDevicesData()
    time.sleep(0.5)
    
    # Send command to start servo motor.
    sendCmd(startCommand)
    
    # Collect data
    sData.snifferMain(fileName, collectionTime)
    time.sleep(1.)
    # Stop the motor (by reinitialising and setting the amplitude again)
    sendCmd(stopCommand)

if __name__ == "__main__":
    initSerialDevices()
    time.sleep(5)
    freq = float(sys.argv[1])
    amplitude = float(sys.argv[2])
    if freq==0.001:
        collectionTime = ((1. / freq) * 4 + 5)
        amplitude = float(sys.argv[2])
        print(collectionTime)
    if 0.001<freq <= 0.01:
        collectionTime = ((1. / freq) * 5 + 5)
        amplitude = float(sys.argv[2])
    if 0.01<freq <= 1.0:
        collectionTime = ((1. / freq) * 10 + 5)
        amplitude = float(sys.argv[2])
    if  freq > 1.0:
        collectionTime = 10
        amplitude = float(sys.argv[2])
        
    print(collectionTime)
    commandMain(amplitude, freq, collectionTime)
        
        
