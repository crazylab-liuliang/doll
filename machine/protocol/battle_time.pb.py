class battle_time:

battle_time = int(0)
turn_time = int(0)

def _ready():
	pass

def name():
	return 'battle_time'

def id():
	return 12

def length():
	return 8 ;

def send(stream):
	var buf = ByteBuf.new()
	buf.write_i32(int(id()))
	buf.write_i32(int(length()))
	buf.write_i32(battle_time)
	buf.write_i32(turn_time)
	buf.write_byte(64)
	buf.write_byte(64)
	stream.put_data(buf.raw_data())

def parse_data( byteBuffer):
	battle_time = byteBuffer.read_i32();
	turn_time = byteBuffer.read_i32();
	pass
