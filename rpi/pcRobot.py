#Communication between pcWrapper and arduinoWrapper without threading..
import thread
import time
import serial

from pcWrapper import *
from androidWrapper import *
from arduinoWrapper import *
from collections import deque

pcWrap = pcWrapper()
serWrap = arduinoWrapper()

pcWrap.startIPService()
serWrap.startSerialService()
print "PC and Serial Connection UP..."

while 1:
	#pc give command to arduino move
	msg = pcWrap.read()
	#print "%s: read from wifi: %s" % (time.ctime(), msg)
	serWrap.write(msg)
	#time.sleep(1)

	#arduino feed the sensor readings
	msg2 = serWrap.read()
	#print "%s: read from serial: %s" % (time.ctime(), msg2)
	pcWrap.write(msg2)
#time.sleep(1)

