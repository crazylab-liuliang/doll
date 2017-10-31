class on_attacked:

damage = int(0)

def _ready():
	pass

def name():
	return 'on_attacked'

def id():
	return 20

def length():
	return 4 ;

def send(stream):
	var buf = ByteBuf.new()
	buf.write_i32(int(id()))
	buf.write_i32(int(length()))
	buf.write_i32(damage)
	buf.write_byte(64)
	buf.write_byte(64)
	stream.put_data(buf.raw_data())

def parse_data( byteBuffer):
	damage = byteBuffer.read_i32();
	pass
