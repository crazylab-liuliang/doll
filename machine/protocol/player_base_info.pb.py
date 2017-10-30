class player_base_info:

cur_blood = int(0)
max_blood = int(0)

def _ready():
	pass

def name():
	return 'player_base_info'

def id():
	return 21

def length():
	return 8 ;

def send(stream):
	var buf = ByteBuf.new()
	buf.write_i32(int(id()))
	buf.write_i32(int(length()))
	buf.write_i32(cur_blood)
	buf.write_i32(max_blood)
	buf.write_byte(64)
	buf.write_byte(64)
	stream.put_data(buf.raw_data())

def parse_data( byteBuffer):
	cur_blood = byteBuffer.read_i32();
	max_blood = byteBuffer.read_i32();
	pass
