extends Node

var type = int(0)
var op = int(0)

func name():
	return 'machine_control'

func id():
	return 19

func length():
	return 8 ;

func send(stream):
	var buf = ByteBuf.new()
	buf.write_i32(int(id()))
	buf.write_i32(int(length()))
	buf.write_i32(type)
	buf.write_i32(op)
	buf.write_byte(64)
	buf.write_byte(64)
	stream.put_data(buf.raw_data())

func parse_data( byteBuffer):
	type = byteBuffer.read_i32();
	op = byteBuffer.read_i32();
	pass
