class ranking_response:

ranking = String()

def _ready():
	pass

def name():
	return 'ranking_response'

def id():
	return 24

def length():
	return 4 +ranking.length();

def send(stream):
	var buf = ByteBuf.new()
	buf.write_i32(int(id()))
	buf.write_i32(int(length()))
	buf.write_string(ranking)
	buf.write_byte(64)
	buf.write_byte(64)
	stream.put_data(buf.raw_data())

def parse_data( byteBuffer):
	ranking = byteBuffer.read_string();
	pass
