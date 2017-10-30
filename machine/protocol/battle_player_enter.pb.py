class battle_player_enter:

player = -1
name = String()
pos = int(0)

def _ready():
	pass

def name():
	return 'battle_player_enter'

def id():
	return 6

def length():
	return 16 +name.length();

def send(stream):
	var buf = ByteBuf.new()
	buf.write_i32(int(id()))
	buf.write_i32(int(length()))
	buf.write_i64(player)
	buf.write_string(name)
	buf.write_i32(pos)
	buf.write_byte(64)
	buf.write_byte(64)
	stream.put_data(buf.raw_data())

def parse_data( byteBuffer):
	player = byteBuffer.read_i64();
	name = byteBuffer.read_string();
	pos = byteBuffer.read_i32();
	pass
