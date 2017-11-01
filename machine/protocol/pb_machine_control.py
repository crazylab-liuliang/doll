import struct

class machine_control:
type = int(0)

	def name(self):
		return 'machine_control'

	def id(self):
		return 19

	def length(self):
		return 4 ;

	def send(self, stream):
		buf = struct.pack('!ii!iBB', self.id(), self.length(),type,64,64)
		stream.send(buf)

	def parse_data(self, byteBuffer):
	type = byteBuffer.read_i32();
		return
