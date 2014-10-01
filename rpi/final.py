import thread
import time
import serial

from pcWrapper import *
from androidWrapper import *
from arduinoWrapper import *
from collections import deque

pcWrap = pcWrapper()
serWrap = arduinoWrapper()
btWrap = androidWrapper()

pcWrap.startIPService()
#serWrap.startSerialService()
#btWrap.startBTService()
print "BT, PC and Serial Connection UP..."

msg = pcWrap.read()

msg="hey"
while(msg!="START"):
	#msg = btWrap.read()
	pcWrap.write(msg)

while 1:
	#pc give command to arduino move
	msg = pcWrap.read()
	if (msg == "done/"):
		print "break out"
		break;
	#btWrap.write(msg)
	#serWrap.write(msg)

	#arduino feed the sensor readings
	#msg2 = serWrap.read()
	msg2 = "hello"
	pcWrap.write(msg2)
	#btWrap.write(msg2)

	msg="hey"
while(msg!="START"):
	#msg = btWrap.read()
	pcWrap.write(msg)

while 1:
	#pc give command to arduino move
	msg = pcWrap.read()
	#btWrap.write(msg)
	#serWrap.write(msg)

	#arduino feed the sensor readings
	#msg2 = serWrap.read()
	msg2 = "og"
	pcWrap.write(msg2)
	#btWrap.write(msg2)