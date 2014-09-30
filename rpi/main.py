import thread

from collections import deque
from androidWrapper import *
from pcWrapper import *
from arduinoWrapper import *

class Main:

	def __init__(self):
		self.android = androidWrapper()
		self.pc = pcWrapper()
		self.arduino = arduinoWrapper()

		self.ipq = deque([])
		self.btq = deque([])
		self.serialq = deque([])

	def ipWrite (self, delay, pc, ipq):
		stop_flag = 0
		while stop_flag == 0:
			time.sleep (delay)
			if len(ipq) >0:
				msg = ipq.popleft()
				print "BT queue length after pop: " , len(ipq)
				pc.write(msg)
				print "%s: %s --msg: %s" % ("ipWrite", time.ctime(time.time()), msg)

	def ipRead (self, delay, pc, btq, serialq):
		stop_flag = 0
		while stop_flag == 0:
			time.sleep (delay)
			#if pc.read()!=None:
			msg = pc.read()
			btq.append(msg)
			serialq.append(msg)
			print "%s: %s--msg: %s" % ("ipRead", time.ctime(time.time()),msg )

	def btWrite (self, delay, android, btq):
		stop_flag = 0
		while stop_flag == 0:
			time.sleep (delay)
			if len(btq) >0:
				msg = btq.popleft()
				print "bt queue length after pop: " , len(btq)
				android.write(msg)
				print "%s: %s --msg: %s" % ("btWrite", time.ctime(time.time()), msg)

	def btRead (self, delay, android, ipq)
		stop_flag = 0
		while stop_flag == 0:
			time.sleep (delay)
			#if android.read()!=None:
			msg = android.read()
			ipq.append(msg)
			print "ip queue length after append: ", len(ipq)
			print "%s: %s--msg: %s" % ("btRead", time.ctime(time.time()),msg )

	def serialWrite(self, delay, arduino, serialq):
		stop_flag = 0
		while stop_flag == 0:
			if len(serialq) > 0:
				msg = serialq.popleft()
				time.sleep(delay)
				arduino.write(msg)
				print "Serial queue length after append: ", len(serialq)
				print "%s: %s--msg: %s" % ("serialRead", time.ctime(time.time()),msg )

	def serialRead(self, delay, arduino, ipq, btq):
		stop_flag = 0
		while stop_flag == 0:
			time.sleep(delay)
			#if arduino.read() !=None: #check for empty string/char when reading.
			msg = arduino.read()
			#append the msg to both bluetooth queue and ip queue
			btq.append(msg)
			ipq.append(msg)
			print "BT queue length after append: ", len(btq)
			print "IP queue length after append: ", len(ipq)
			print "%s: %s--msg: %s" % ("serialRead", time.ctime(time.time()),msg )

	def startServices(self):
		ready1=[False]
		ready2=[False]
		ready3=[False]
		thread.start_new_thread(self.android.startBTService, (1.0,ready1))
		thread.start_new_thread(self.pc.startIPService, (1.0,ready2))
		thread.start_new_thread(self.arduino.startSerialService, (1.0,ready3))
		while True:
			if ready1[0]!=True or ready2[0]!=True or ready3[0]!=True:
				pass
			else:
				print "break off"
				time.sleep(3)
				break

	def mainStart(self):
		print "entering mainStart"
		thread.start_new_thread (self.ipWrite, (0.5, self.pc, self.ipq))
		thread.start_new_thread (self.ipRead,  (0.5, self.pc, self.btq, self.serialq))
		thread.start_new_thread (self.btWrite, (0.5, self.android, self.btq))
		#thread.start_new_thread (self.btRead,  (0.5, self.android, self.btq))
		thread.start_new_thread (self.serialWrite, (0.5, self.arduino, self.serialq))
		thread.start_new_thread (self.serialRead,  (0.5, self.arduino, self.ipq, self.btq))
		#except:
		while True:
			time.sleep(4.0)


test = Main()
test.startServices()
test.mainStart()