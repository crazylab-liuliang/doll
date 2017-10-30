class battle_player_blood:

self_blood = int(0)
enemy_blood = int(0)

def _ready():
	pass

def name():
	return 'battle_player_blood'

def id():
	return 5

def length():
	return 8 ;

def send(stream):
	var buf = ByteBuf.new()
	buf.write_i32(int(id()))
	buf.write_i32(int(length()))
	buf.write_i32(self_blood)
	buf.write_i32(enemy_blood)
	buf.write_byte(64)
	buf.write_byte(64)
	stream.put_data(buf.raw_data())

def parse_data( byteBuffer):
	self_blood = byteBuffer.read_i32();
	enemy_blood = byteBuffer.read_i32();
	pass
