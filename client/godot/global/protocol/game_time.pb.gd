extends Node

var time = int(0)

func name():
	return 'game_time'

func id():
	return 14

func length():
	return 4 ;

func send(stream):
	var buf = ByteBuf.new()
	buf.write_i32(int(id()))
	buf.write_i32(int(length()))
	buf.write_i32(time)
	buf.write_byte(64)
	buf.write_byte(64)
	stream.put_data(buf.raw_data())

func parse_data( byteBuffer):
	time = byteBuffer.read_i32();
	pass
