import struct

class machine_login:

def _ready():
	pass

def name():
	return 'machine_login'

def id():
	return 19

def length():
	return 0 ;

def send(stream):
	buf = struct.pack('iiBB',id(),length(),64,64)
	stream.send(buf)

def parse_data( byteBuffer):
	return
