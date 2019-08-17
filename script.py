import serial
from datetime import datetime


roll_no = str(raw_input())

sensor = "ECG"
serial_port = '/dev/ttyACM0'
roll_no += ".txt"
baud_rate = 115200
ser = serial.Serial(serial_port, baud_rate)
print ("start time ")
print (datetime.now())
with open(roll_no, 'w+') as f:
    while True:
            line = ser.readline()
            f.writelines([line.strip(), " t = %s \n " % (datetime.now())])

print (datetime.now())
print ("end time")