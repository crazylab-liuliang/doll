extends Node

var result = int(0)

func name():
	return 'search_room_result'

func id():
	return 31

func length():
	return 4 ;

func send(stream):
	var buf = ByteBuf.new()
	buf.write_i32(int(id()))
	buf.write_i32(int(length()))
	buf.write_i32(result)
	buf.write_byte(64)
	buf.write_byte(64)
	stream.put_data(buf.raw_data())

func parse_data( byteBuffer):
	result = byteBuffer.read_i32();
	pass
