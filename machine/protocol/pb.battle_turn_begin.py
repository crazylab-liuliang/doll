class battle_turn_begin:

player = -1

def _ready():
	pass

def name():
	return 'battle_turn_begin'

def id():
	return 13

def length():
	return 8 ;

def send(stream):
	var buf = ByteBuf.new()
	buf.write_i32(int(id()))
	buf.write_i32(int(length()))
	buf.write_i64(player)
	buf.write_byte(64)
	buf.write_byte(64)
	stream.put_data(buf.raw_data())

def parse_data( byteBuffer):
	player = byteBuffer.read_i64();
	pass
