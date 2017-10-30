class max_score:

max_score = int(0)

def _ready():
	pass

def name():
	return 'max_score'

def id():
	return 19

def length():
	return 4 ;

def send(stream):
	var buf = ByteBuf.new()
	buf.write_i32(int(id()))
	buf.write_i32(int(length()))
	buf.write_i32(max_score)
	buf.write_byte(64)
	buf.write_byte(64)
	stream.put_data(buf.raw_data())

def parse_data( byteBuffer):
	max_score = byteBuffer.read_i32();
	pass
