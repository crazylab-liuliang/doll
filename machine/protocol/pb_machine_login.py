import struct

class machine_login:

	def name(self):
		return 'machine_login'

	def id(self):
		return 20

	def length(self):
		return 0 ;

	def send(self, stream):
		buf = struct.pack('!iiBB', self.id(), self.length(),64,64)
		stream.send(buf)

	def data(self):
		buf = struct.pack('!iiBB', self.id(), self.length(),64,64)
		return buf

	def parse_data(self, byteBuffer):
		return
