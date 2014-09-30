import serial

class serialWrapper:
	def __init__(self):
		print "init arduino port and baud"
		#\dev\ttyACM0 in RPi
		self.port = '/dev/ttyACM0'
		#depend on what arduino set for the baud rate..
		self.baud = 115200

	def connect(self):
		#connect to serial socket
		print "Connecting Serial..."
		#sersock object name for Serial
		self.sersock = serial.Serial (self.port, self.baud)
		#init the connection
		#self.sersock.write('')
		#self.sersock.write('')
		print "Serial Socket linked up"

	def disconnect(self):
		self.sersock.close()

	def write(self, msg):
		self.sersock.write(msg)
		print "Writing to Arduino: %s" %(msg)

	def read(self):
		#put the read line to a String type msg
		msg = self.sersock.readline()
		print "Reading from Arduino: %s" %(msg)
		#return the message
		return msg

#test
test = serialWrapper()
test.connect()
test.write('F')