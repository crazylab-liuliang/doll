class register_by_email:

password = String()
email = String()

def _ready():
	pass

def name():
	return 'register_by_email'

def id():
	return 25

def length():
	return 8 +password.length()+email.length();

def send(stream):
	var buf = ByteBuf.new()
	buf.write_i32(int(id()))
	buf.write_i32(int(length()))
	buf.write_string(password)
	buf.write_string(email)
	buf.write_byte(64)
	buf.write_byte(64)
	stream.put_data(buf.raw_data())

def parse_data( byteBuffer):
	password = byteBuffer.read_string();
	email = byteBuffer.read_string();
	pass
