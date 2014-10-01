
import thread
import time
import serial

from interface import *
from pc_interface import *
from android_interface import *
from arduino_interface import *
from collections import deque

pc_in = pc_interface()
ser = arduino_interface()

pc_in.connect()
ser.connect()
print "All connections up"

#command = []
#command.append("f050/")
#command.append("r000/")
#command.append("f050/")
#command.append("l000/")
#command.append("f050/")


while 1:
	#pc give command to arduino move
	msg = pc_in.read()
	#print "%s: read from wifi: %s" % (time.ctime(), msg)
	ser.write(msg)
	#time.sleep(1)

	#arduino feed the sensor readings
	msg2 = ser.read()
	#print "%s: read from serial: %s" % (time.ctime(), msg2)
	pc_in.write(msg2)
#time.sleep(1)

