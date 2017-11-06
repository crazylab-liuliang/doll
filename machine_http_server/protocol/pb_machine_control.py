import struct

class machine_control:
	type = int(0)
	op = int(0)

	def name(self):
		return 'machine_control'

	def id(self):
		return 19

	def length(self):
		return 8 ;

	def send(self, stream):
		buf = struct.pack('!iiiiBB', self.id(), self.length(),self.type,self.op,64,64)
		stream.send(buf)

	def parse_data(self, byteBuffer):
		self.type,self.op = struct.unpack( "!ii", byteBuffer)
		return
