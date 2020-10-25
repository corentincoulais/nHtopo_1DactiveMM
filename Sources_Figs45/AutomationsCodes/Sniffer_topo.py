__linux_serialdeviceData__ = "/dev/ttyACM1"





#pic the right connections in the right order
__win_serialdeviceData1__ = "COM22"
__win_serialdeviceData5__ = "COM27"
__win_serialdeviceData7__ = "COM31"
__win_serialdeviceData9__ = "COM28"


import time
import sys, os
import serial
import csv
import re

def initSerialDevicesData():
    global serData1, serData2, serData3, serData4, serData5, serData6, serData7, serData8, serData9, serData10

    if os.name=="posix":
        # This part is ignored since this computer works with windows.
        serData = serial.Serial(__linux_serialdeviceData__, 115200, timeout=2.0)
        print("serial device %s initialized"%__linux_serialdeviceData__)
    else:
        serData1 = serial.Serial(__win_serialdeviceData1__, 115200, timeout=2.0)
        print("serial device %s initialized"%__win_serialdeviceData1__)
        serData5 = serial.Serial(__win_serialdeviceData5__, 115200, timeout=2.0)
        print("serial device %s initialized"%__win_serialdeviceData5__)
        serData7 = serial.Serial(__win_serialdeviceData7__, 115200, timeout=2.0)
        print("serial device %s initialized"%__win_serialdeviceData7__)
        serData9 = serial.Serial(__win_serialdeviceData9__, 115200, timeout=2.0)
        print("serial device %s initialized"%__win_serialdeviceData9__)

        serData1.reset_output_buffer()
        serData5.reset_output_buffer()
        serData7.reset_output_buffer()
        serData9.reset_output_buffer()
        

def getData():
    global  serData1, serData5, serData7, serData9, datafile #serData1,serData3
    dataStr = ""
    print ("ik ben hier")
    s1 = serData1.readline()
    s5 = serData5.readline()
    s7 = serData7.readline()
    s9 = serData9.readline()
    print(s1, s5, s7, s9)
    dataStr = s1+s5+s7+s9
  
    dataStr = re.sub("\r\n", ',', dataStr.decode('utf-8'))
    dataStr = dataStr[:-1]
    print(dataStr)
    data = [int(y) for y in dataStr.split(',')]
    print (data)
    print ("ik ben hier")
    if datafile != "":
        #converting the data to degrees. 
        
        datafile.write(",".join(str((y-4000.)*(100.0/4000.)) for y in data))
        datafile.write("\n")
        datafile.flush()

def snifferMain(filename, collectionTime):
    global datafile
    time.sleep(1)
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    if filename != "":
        
        filePath = os.path.join(fileDir, 'captureDump/' + filename)
        datafile = open(filePath, "w")
    else:    
       datafile = ""
    print("Getting data.....")
    
    
    endTime = time.time() + collectionTime + 1
    time.sleep(5)
    while time.time() < endTime:
        getData()
        


if __name__ == "__main__":
    initSerialDevicesData()
    fileName = str(input("filename to store data:"))
    collectionTime = float(input("collection time in seconds:"))
    snifferMain(fileName, collectionTime)
    

