import struct

class machine_move_left:

	def name(self):
		return 'machine_move_left'

	def id(self):
		return 20

	def length(self):
		return 0 ;

	def send(self, stream):
		buf = struct.pack('!iiBB', self.id(), self.length(),64,64)
		stream.send(buf)

	def parse_data(self, byteBuffer):
		return
