import serial
import bluetooth
import thread
import time
import socket
from collections import deque

from pythonBTserver import * #class is androidWrapper
from pythonWiFiserver import * #class is pcWrapper
#from pythonSerial_Arduino import * #class is serialWrapper

#define functions for the settings of IPComm, SerComm, BTComm
def setIPComm():
	#depend on your RPi IP address 192.168.x.x
	#either 18.1 or 18.21
	UDP_IP = "192.168.18.21"
	UDP_PORT = 5143
	ipsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	#re-usable port
	ipsock.setsockopt (socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	ipsock.setsockopt (socket.SOL_SOCKET, socket.SO_BROADCAST,1)
	ipsock.bind((UDP_IP, UDP_PORT))
	data, pcaddr = ipsock.recvfrom (1024)
	print "CONNECTED...", pcaddr
	return ipsock, pcaddr

def setSerComm():
	#establish the connection with arduino via Serial
	sersock = serial.Serial('/dev/ttyACM0', 115200)
    	return sersock

def setBTComm ():
	#establish the bluetooth connection
	#the N7 BT mac address
	btaddr = "08:60:6E:A4:E4:D4"
    	port = 3
    	btsock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    	btsock.connect((btaddr, port))
    	return btsock

class main:
	#define the 
	def __init__(self):
	#start init the communication: Android, Arduino and PC
		self.android = androidWrapper()
		self.pc = pcWrapper()
		
		#queue
		self.ipq = deque([])
		self.serq = deque([])
		self.btq = deque([])

	def ipWrite (threadName, delay, pc, ipq):
		stop_flag = 0
		while stop_flag == 0:
			time.sleep (delay)
			print "WiFi queue length: ", len(ipq)
			if len(ipq) >0:
				msg = ipq.popleft()
				pc.write()
				print "%s: %s --msg: %s" % (threadName, time.ctime(time.time()), msg)

	def ipRead(threadName, delay):
		stop_flag = 0
		buff = 1024
		while stop_flag == 0:
			
