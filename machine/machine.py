import serial
import time
import random
import protocol.pb_machine_control as pb_mc

def hex2int(str):
	return int(str.encode('hex'), 16)

class dollmachine:
	ser = None
	loop_time = 0.0
	data_buffer = []
	pid = 0
	header_size = 7

	def __init__(self):
		self.ser = serial.Serial("/dev/ttyUSB0", 115200, timeout=10, stopbits=serial.STOPBITS_ONE, rtscts=False, dsrdtr=False)
		return

	def __del__(self):
		self.cleanup()

	def cleanup(self):
		if self.ser != None:
			self.ser.close()

		return
	

	def rand_pid(self):
		self.pid = 0
		rd  = random.randint(0, 65025)
		while self.pid==rd:
			rd = random.randint(0, 65025)

		self.pid = rd

	def on_recv_machine_control(self, msg):
		if msg.type==0:
			self.add_coin()

		if msg.type==1:
			self.set_forward(msg.op)

		if msg.type==2:
			self.set_back(msg.op)

		if msg.type==3:
			self.set_left(msg.op)

		if msg.type==4:
			self.set_right(msg.op)

		if msg.type==5:
			self.take_doll()

	def add_coin(self):	
		self.rand_pid()
		data = bytearray([0xfe, self.pid/255, self.pid%255, 0x01, (~(self.pid/255))&0xff, (~(self.pid%255))&0xff, 0x14, 0x31, 0x3c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x09, 0x21, 0x00,0x00, 0x00, 0x47])
		self.ser.write( data)
		time.sleep(0.1)
		print("add coin...")

	def set_stop(self):
		self.rand_pid()
		data = bytearray([0xfe, self.pid/255, self.pid%255, 0x01, (~(self.pid/255))&0xff, (~(self.pid%255))&0xff, 0x0c, 0x32, 0x05, 0x00, 0x00, 0x43])
		self.ser.write( data)


	def set_forward(self, value):
		if value!=0:
			self.rand_pid()
			data = bytearray([0xfe, self.pid/255, self.pid%255, 0x01, (~(self.pid/255))&0xff, (~(self.pid%255))&0xff, 0x0c, 0x32, 0x00, 0x00, 0x14, 0x52])
			self.ser.write( data)
			print("forward begin")
			time.sleep(0.1)
		else:
			self.set_stop()
			print("forward stop")

	def set_back(self, value):
		if value!=0:
			self.rand_pid()
			data = bytearray([0xfe, self.pid/255, self.pid%255, 0x01, (~(self.pid/255))&0xff, (~(self.pid%255))&0xff, 0x0c, 0x32, 0x01, 0x00, 0x14, 0x53])
			self.ser.write( data)
			time.sleep(0.1)
			print("back begin")
		else:
			self.set_stop()
			print("back stop")

	def set_left(self, value):
		if value!=0:
			self.rand_pid()
			data = bytearray([0xfe, self.pid/255, self.pid%255, 0x01, (~(self.pid/255))&0xff, (~(self.pid%255))&0xff, 0x0c, 0x32, 0x02, 0x00, 0x14, 0x54])
			self.ser.write( data)
			time.sleep(0.1)
			print("left begin")
		else:
			self.set_stop()
			print("left stop")

	def set_right(self, value):
		if value!=0:
			self.rand_pid()
			data = bytearray([0xfe, self.pid/255, self.pid%255, 0x01, (~(self.pid/255))&0xff, (~(self.pid%255))&0xff, 0x0c, 0x32, 0x03, 0x00, 0x14, 0x55])
			self.ser.write( data)
			time.sleep(0.1)
			print("right begin")
		else:
			self.set_stop()
			print("right stop")

	def take_doll(self):
		self.rand_pid()
		data = bytearray([0xfe, self.pid/255, self.pid%255, 0x01, (~(self.pid/255))&0xff, (~(self.pid%255))&0xff, 0x0c, 0x32, 0x04, 0x00, 0x00, 0x42])
		self.ser.write( data)
		print("take doll")
		time.sleep(0.1)

	def process_rcv_bytes(self):
		# make sure msg begin weith 0xfe		
		while len(self.data_buffer) > 1 and self.data_buffer[0] != '\xfe':
			print("error : protocol begin with ["+ self.data_buffer[0] + "], it should begin with [0xfe]...")
			self.data_buffer = self.data_buffer[1:]

		# make sure we can get data  len from header size
		if len(self.data_buffer) < self.header_size:
			return

		proto_head = self.data_buffer[:self.header_size]
		proto_size = hex2int(proto_head[self.header_size-1])

		if len(self.data_buffer) < proto_size:
				return

		proto_body = self.data_buffer[self.header_size : proto_size]
		self.process_rcv_pack(proto_head, proto_body)

		self.data_buffer = self.data_buffer[proto_size:]


	def process_rcv_pack(self, head, body):
		msg_type = hex2int(body[0])
		if msg_type == 0x03 or msg_type == 0x33:
			catch_result = hex2int(body[1])
			if catch_result == 0x00:
				print("catch nothing...\n")
			elif catch_result==0x01:
				print("catch one doll...\n")

	def loop(self, delta):		
		self.loop_time += delta
		if self.loop_time > 1:
			inbuff = self.ser.in_waiting
			while inbuff > 0:
				self.data_buffer += self.ser.read(inbuff)
				inbuff = self.ser.in_waiting

			self.process_rcv_bytes()
				
			self.loop_time =0.0

