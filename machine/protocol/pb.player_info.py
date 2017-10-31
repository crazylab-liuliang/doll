class player_info:

player = -1
name = String()

def _ready():
	pass

def name():
	return 'player_info'

def id():
	return 22

def length():
	return 12 +name.length();

def send(stream):
	var buf = ByteBuf.new()
	buf.write_i32(int(id()))
	buf.write_i32(int(length()))
	buf.write_i64(player)
	buf.write_string(name)
	buf.write_byte(64)
	buf.write_byte(64)
	stream.put_data(buf.raw_data())

def parse_data( byteBuffer):
	player = byteBuffer.read_i64();
	name = byteBuffer.read_string();
	pass
