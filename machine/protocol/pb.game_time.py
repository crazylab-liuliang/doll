class game_time:

time = int(0)

def _ready():
	pass

def name():
	return 'game_time'

def id():
	return 14

def length():
	return 4 ;

def send(stream):
	var buf = ByteBuf.new()
	buf.write_i32(int(id()))
	buf.write_i32(int(length()))
	buf.write_i32(time)
	buf.write_byte(64)
	buf.write_byte(64)
	stream.put_data(buf.raw_data())

def parse_data( byteBuffer):
	time = byteBuffer.read_i32();
	pass
