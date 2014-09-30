import serial
import time

class arduinoWrapper:

    def __init__(self):
        self.port = '/dev/ttyACM0'
        self.baud = 115200

    def startSerialService(self, delay, ready3):
		print "Waiting for Serial Connection..."
		self.serSock = serial.Serial (self.port, self.baud)
        #init socket connection
        #self.serSock.write("")
        #self.serSock.write("")
        print "Serial Connection Link Up..."
		ready3[0]=True
		#return True

    def startSerialService(self):
		print "Waiting for Serial Connection..."
        self.serSock = serial.Serial (self.port, self.baud)
        #init socket connection
        #self.serSock.write("")
        #self.serSock.write("")
        print "Serial Connection Link Up..."
		return True
		
    def stopSerialService(self):
        self.serSock.close()

    def write(self,msg):
		if self.serSock.getCTS() == True:
			self.serSock.write(msg)
			print "Write to Arduino: %s" %(msg)

    def read(self):
        msg = self.serSock.readline()
		print "%s" %(self.serSock.inWaiting())
        print "Read from Arduino: %s" %(msg)
        return msg
		
test = arduinoWrapper()
if test.startSerialService() == True:
	time.sleep(3)
	test.write('F')
	time.sleep(3)
	test.read()
	time.sleep(3)
	test.write('L')
	test.read()
	time.sleep(3)
test.stopSerialService()