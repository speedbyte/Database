#!/usr/bin/env python
import socket
import time
import random

UDP_IP = "127.0.0.1"
UDP_PORT = 5000

t = time.time()
#Sys. time in UNIX epoch
tim_S = "Time"+str(t)[:-3]+"\n"
tim_M = "Time"+str(t*.01)[-3:]+"\n"
#random ACC values
ACC_X = "AccX"+str(random.randint(-25500,25500)*0.01)+"\n"
ACC_Y = "AccY"+str(random.randint(-25500,25500)*0.01)+"\n"
ACC_Z = "AccZ"+str(random.randint(-25500,25500)*0.01)+"\n"
#random MAG values
MAG_X = "MagX"+str(random.randint(-25500,25500)*0.01)+"\n"
MAG_Y = "MagY"+str(random.randint(-25500,25500)*0.01)+"\n"
MAG_Z = "MagZ"+str(random.randint(-25500,25500)*0.01)+"\n"
#random GYRO values
G_YAW = "GyrY"+str(random.randint(-25500,25500)*0.01)+"\n"
G_PITCH = "GyrP"+str(random.randint(-25500,25500)*0.01)+"\n"
G_ROLL= "GyrR"+str(random.randint(-25500,25500)*0.01)+"\n"
#random TEMP and PRESS values
TEMP = "Temp"+str(random.randint(-25500,25500)*0.01)+"\n"
PRESS = "Pres"+str(random.randint(-25500,25500)*0.01)+"\n"
#ramdom MOTOR values
M1 = "M1"+str(random.randint(-25500,25500)*0.01)+"\n"
M2 = "M2"+str(random.randint(-25500,25500)*0.01)+"\n"
M3 = "M3"+str(random.randint(-25500,25500)*0.01)+"\n"
M4 = "M4"+str(random.randint(-25500,25500)*0.01)

MESSAGE = tim_S+tim_M+ACC_X+ACC_Y+ACC_Z+MAG_X+MAG_Y+MAG_Z+G_YAW+G_PITCH+G_ROLL+TEMP+PRESS+M1+M2+M3+M4

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
