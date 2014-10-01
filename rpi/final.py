import thread
import time
import serial

from interface import *
from pc_interface import *
from android_interface import *
from arduino_interface import *
from collections import deque

wifi = pc_interface()
ser = arduino_interface()
bt = android_interface()

bt.connect()
wifi.connect()
ser.connect()
print "All connections up"

#command = []
#command.append("f050/")
#command.append("r000/")
#command.append("f050/")
#command.append("l000/")
#command.append("f050/")

#msg = ""

#while(msg!="btstart"):
#	msg = bt.read()

msg = wifi.read()

msg="hey"
while(msg!="btstart"):
	msg = bt.read()
	wifi.write(msg)

while 1:
	#pc give command to arduino move
	msg = wifi.read()
	if (msg == "done/"):
		break;
	bt.write(msg)
	ser.write(msg)

	#arduino feed the sensor readings
	msg2 = ser.read()
	wifi.write(msg2)
	bt.write(msg2)

	msg="hey"
while(msg!="btstart"):
	msg = bt.read()
	wifi.write(msg)

while 1:
	#pc give command to arduino move
	msg = wifi.read()
	bt.write(msg)
	ser.write(msg)

	#arduino feed the sensor readings
	msg2 = ser.read()
	wifi.write(msg2)
	bt.write(msg2)