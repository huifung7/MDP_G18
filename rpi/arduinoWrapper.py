import serial
import time

class arduinoWrapper:

    def __init__(self):
        self.port = '/dev/ttyACM0'
        self.baud = 115200

    def startSerialService(self):
        self.serSock = serial.Serial (self.port, self.baud)
        #init socket connection
        #self.serSock.write("")
        #self.serSock.write("")
        print "serial link up"
		return True

    def stopSerialService(self):
        self.serSock.close()

    def write(self,msg):
        self.serSock.write(msg)
        print "Write to Arduino: %s" %(msg)

    def read(self):
        msg = self.serSock.readline()
        print "Read from Arduino: %s" %(msg)
        return msg
		
test = arduinoWrapper()
if test.startSerialService() == True:
	time.sleep(2)
	test.write('F')
	test.write('L')
	time.sleep(0.8)
test.stopSerialService()