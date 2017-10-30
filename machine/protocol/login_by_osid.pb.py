class login_by_osid:

osid = String()

def _ready():
	pass

def name():
	return 'login_by_osid'

def id():
	return 17

def length():
	return 4 +osid.length();

def send(stream):
	var buf = ByteBuf.new()
	buf.write_i32(int(id()))
	buf.write_i32(int(length()))
	buf.write_string(osid)
	buf.write_byte(64)
	buf.write_byte(64)
	stream.put_data(buf.raw_data())

def parse_data( byteBuffer):
	osid = byteBuffer.read_string();
	pass
