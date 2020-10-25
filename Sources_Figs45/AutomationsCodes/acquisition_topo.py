# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 13:46:51 2018

@author: coulais
"""

__linux_serialdeviceCmd__ = "/dev/ttyACM0"
__win_serialdeviceCmd__ = "COM5"
__linux_serialdeviceData__ = "/dev/ttyACM1"
__win_serialdeviceData__ = "COM9"


import numpy as np
import time
import sys, os
import serial
import csv
import re
import simple_serialcommand as sCommand
import simple_serialsniffer as sData
from multiprocessing import Pool

#used for 9 pendula
def acquisitionMainV2(freqList, amplitude):
    for i in range(len(freqList)):
        print("python simple_serialcommand_topo.py " + str(freqList[i]) + " " + str(amplitude))
        os.system("python simple_serialcommand_topo.py " + str(freqList[i]) + " " + str(amplitude))


    
if __name__ == "__main__":

    amplitude = 130
    
    #Data aquisition for 9 pendula:
    acquisitionMainV2([0.1], amplitude)

    
    
