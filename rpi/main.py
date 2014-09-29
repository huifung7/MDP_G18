#import serial
import threading
import bluetooth
import thread
import time
import socket
from collections import deque

from androidWrapper import *
from pcWrapper import *


class Main:

	def __init__(self):
		self.android = androidWrapper()
		self.pc = pcWrapper()
		self.ipq = deque([])
		self.btq = deque([])

	def ipWrite (self, delay, pc, btq):
		stop_flag = 0
		while stop_flag == 0:
			time.sleep (delay)

			if len(btq) >0:
				msg = btq.popleft()
				print "BT queue length after pop: " , len(btq)
				pc.write(msg)
				print "%s: %s --msg: %s" % ("ipWrite", time.ctime(time.time()), msg)


	def ipRead (self, delay, pc, ipq):
		stop_flag = 0
		while stop_flag == 0:
			time.sleep (delay)
			msg = pc.read()
			ipq.append(msg)
			print "IP queue length after append: ", len(ipq)
			print "%s: %s--msg: %s" % ("ipRead", time.ctime(time.time()),msg )

	def btWrite (self, delay, android, ipq):
		stop_flag = 0
		while stop_flag == 0:
			time.sleep (delay)
			if len(ipq) >0:
				msg = ipq.popleft()
				print "IP queue length after pop: " , len(ipq)
				android.write(msg)
				print "%s: %s --msg: %s" % ("btWrite", time.ctime(time.time()), msg)

	def btRead (self, delay, android, btq):
		stop_flag = 0
		while stop_flag == 0:
			time.sleep (delay)
			msg = android.read()
			btq.append(msg)
			print "BT queue length after append: ", len(btq)
			print "%s: %s--msg: %s" % ("btRead", time.ctime(time.time()),msg )

	def startBT():
		self.android.startBTService()
		
	def startIP():
		self.pc.startIPService()
		
	def mainStart(self):
		#try:

		thread.start_new_thread (self.ipWrite, (0.5, self.pc, self.btq))
		thread.start_new_thread (self.ipRead,  (0.5, self.pc, self.ipq))
		thread.start_new_thread (self.btWrite, (0.5, self.android, self.ipq))
		thread.start_new_thread (self.btRead, (0.5, self.android, self.btq))
		#except:
		while True:
			time.sleep(2.0)

test = Main()
btTime = threading.Timer(10.0, startBT)
btTime.start()
ipTime = threading.Timer(10.0, startIP)
ipTime.start() 
test.mainStart()