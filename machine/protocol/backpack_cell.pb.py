class backpack_cell:

item_id = int(0)
index = int(0)
item_num = int(0)

def _ready():
	pass

def name():
	return 'backpack_cell'

def id():
	return 1

def length():
	return 12 ;

def send(stream):
	var buf = ByteBuf.new()
	buf.write_i32(int(id()))
	buf.write_i32(int(length()))
	buf.write_i32(item_id)
	buf.write_i32(index)
	buf.write_i32(item_num)
	buf.write_byte(64)
	buf.write_byte(64)
	stream.put_data(buf.raw_data())

def parse_data( byteBuffer):
	item_id = byteBuffer.read_i32();
	index = byteBuffer.read_i32();
	item_num = byteBuffer.read_i32();
	pass
