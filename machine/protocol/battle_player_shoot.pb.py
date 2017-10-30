class battle_player_shoot:

player = -1
weapon_pos_x = float(0)
weapon_pos_y = float(0)
degree = float(0)

def _ready():
	pass

def name():
	return 'battle_player_shoot'

def id():
	return 8

def length():
	return 20 ;

def send(stream):
	var buf = ByteBuf.new()
	buf.write_i32(int(id()))
	buf.write_i32(int(length()))
	buf.write_i64(player)
	buf.write_float(weapon_pos_x)
	buf.write_float(weapon_pos_y)
	buf.write_float(degree)
	buf.write_byte(64)
	buf.write_byte(64)
	stream.put_data(buf.raw_data())

def parse_data( byteBuffer):
	player = byteBuffer.read_i64();
	weapon_pos_x = byteBuffer.read_float();
	weapon_pos_y = byteBuffer.read_float();
	degree = byteBuffer.read_float();
	pass
