class search_room_result:

result = int(0)

def _ready():
	pass

def name():
	return 'search_room_result'

def id():
	return 29

def length():
	return 4 ;

def send(stream):
	var buf = ByteBuf.new()
	buf.write_i32(int(id()))
	buf.write_i32(int(length()))
	buf.write_i32(result)
	buf.write_byte(64)
	buf.write_byte(64)
	stream.put_data(buf.raw_data())

def parse_data( byteBuffer):
	result = byteBuffer.read_i32();
	pass
