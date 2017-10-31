class battle_player_shoot_result:

player1_blood = int(0)
player0_blood = int(0)

def _ready():
	pass

def name():
	return 'battle_player_shoot_result'

def id():
	return 9

def length():
	return 8 ;

def send(stream):
	var buf = ByteBuf.new()
	buf.write_i32(int(id()))
	buf.write_i32(int(length()))
	buf.write_i32(player1_blood)
	buf.write_i32(player0_blood)
	buf.write_byte(64)
	buf.write_byte(64)
	stream.put_data(buf.raw_data())

def parse_data( byteBuffer):
	player1_blood = byteBuffer.read_i32();
	player0_blood = byteBuffer.read_i32();
	pass
