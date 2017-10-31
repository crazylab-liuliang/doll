class register_result:

account = int(0)
result = int(0)

def _ready():
	pass

def name():
	return 'register_result'

def id():
	return 26

def length():
	return 8 ;

def send(stream):
	var buf = ByteBuf.new()
	buf.write_i32(int(id()))
	buf.write_i32(int(length()))
	buf.write_i32(account)
	buf.write_i32(result)
	buf.write_byte(64)
	buf.write_byte(64)
	stream.put_data(buf.raw_data())

def parse_data( byteBuffer):
	account = byteBuffer.read_i32();
	result = byteBuffer.read_i32();
	pass
