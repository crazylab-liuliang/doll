class battle_sync_aim_degree:

aim_degree = float(0)

def _ready():
	pass

def name():
	return 'battle_sync_aim_degree'

def id():
	return 11

def length():
	return 4 ;

def send(stream):
	var buf = ByteBuf.new()
	buf.write_i32(int(id()))
	buf.write_i32(int(length()))
	buf.write_float(aim_degree)
	buf.write_byte(64)
	buf.write_byte(64)
	stream.put_data(buf.raw_data())

def parse_data( byteBuffer):
	aim_degree = byteBuffer.read_float();
	pass
