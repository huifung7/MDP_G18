import socket


class pcWrapper:
	def __init__(self):
		self.tcp_ip = "192.168.18.21"
		self.port = 5143
	
	def startIPService(self):
		self.ipSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		
		self.ipSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
		self.ipSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
		self.ipSocket.bind((self.tcp_ip, self.port))
		print "waiting..."
		self.pcaddr = self.ipSocket.recvfrom(1024)[1]
		print "wifi link up"
		
	def disconnect(self):
		self.ipSocket.close()

	def write(self, msg):
		self.ipSocket.sendto(msg, self.pcaddr)
		print "Write to PC: %s" %(msg)
	
	def read(self):
		msg = self.ipSocket.recvfrom(1024)[0]
		print "Read from PC: %s" % (msg)
		return msg


