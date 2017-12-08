import serial
import time
import random
import protocol.pb_machine_control as pb_mc


class dollmachine:
	ser = None
	take_time = 0
	pid = 0

	def __init__(self):
		self.ser = serial.Serial("/dev/ttyAMA0", 115200, timeout=10)
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
		print("on recv machine control [%d,%d]" % (msg.type, msg.op))
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
		with serial.Serial("/dev/ttyAMA0", 115200, timeout=1) as ser:		
			self.rand_pid()
			data = bytearray([0xfe, self.pid/255, self.pid%255, 0x01, (~(self.pid/255))&0xff, (~(self.pid%255))&0xff, 0x14, 0x31, 0x3c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x09, 0x21, 0x00,0x00, 0x00, 0x47])
			writebytes = ser.write( data)
			print("add coin...")
			ser.close()
			time.sleep(0.1)


	def set_forward(self, value):
		with serial.Serial("/dev/ttyAMA0", 115200, timeout=1) as ser:	
			if value!=0:
				self.rand_pid()
				data = bytearray([0xfe, self.pid/255, self.pid%255, 0x01, (~(self.pid/255))&0xff, (~(self.pid%255))&0xff, 0x0c, 0x32, 0x00, 0x00, 0x14, 0x52])
				writebytes = ser.write( data)
				print("forward begin")
				ser.close()
				time.sleep(0.1)
			else:
				print("forward stop")
				self.rand_pid()
				data = bytearray([0xfe, self.pid/255, self.pid%255, 0x01, (~(self.pid/255))&0xff, (~(self.pid%255))&0xff, 0x0c, 0x32, 0x05, 0x00, 0x00, 0x43])
				writebytes = ser.write( data)
				ser.close()

	def set_back(self, value):
		with serial.Serial("/dev/ttyAMA0", 115200, timeout=1) as ser:	
			if value!=0:
				self.rand_pid()
				data = bytearray([0xfe, self.pid/255, self.pid%255, 0x01, (~(self.pid/255))&0xff, (~(self.pid%255))&0xff, 0x0c, 0x32, 0x01, 0x00, 0x14, 0x53])
				writebytes = ser.write( data)
				print("back begin")
				ser.close()
				time.sleep(0.1)
			else:
				print("back stop")
				self.rand_pid()
				data = bytearray([0xfe, self.pid/255, self.pid%255, 0x01, (~(self.pid/255))&0xff, (~(self.pid%255))&0xff, 0x0c, 0x32, 0x05, 0x00, 0x00, 0x43])
				writebytes = ser.write( data)
				ser.close()


	def set_left(self, value):
		with serial.Serial("/dev/ttyAMA0", 115200, timeout=1) as ser:	
			if value!=0:
				self.rand_pid()
				data = bytearray([0xfe, self.pid/255, self.pid%255, 0x01, (~(self.pid/255))&0xff, (~(self.pid%255))&0xff, 0x0c, 0x32, 0x02, 0x00, 0x14, 0x54])
				writebytes = ser.write( data)
				print("left begin")
				ser.close()
				time.sleep(0.1)
			else:
				print("left stop")
				self.rand_pid()
				data = bytearray([0xfe, self.pid/255, self.pid%255, 0x01, (~(self.pid/255))&0xff, (~(self.pid%255))&0xff, 0x0c, 0x32, 0x05, 0x00, 0x00, 0x43])
				writebytes = ser.write( data)
				ser.close()

	def set_right(self, value):
		with serial.Serial("/dev/ttyAMA0", 115200, timeout=1) as ser:	
			if value!=0:
				self.rand_pid()
				data = bytearray([0xfe, self.pid/255, self.pid%255, 0x01, (~(self.pid/255))&0xff, (~(self.pid%255))&0xff, 0x0c, 0x32, 0x03, 0x00, 0x14, 0x55])
				writebytes = ser.write( data)
				print("right begin")
				ser.close()
				time.sleep(0.1)
			else:
				self.rand_pid()
				data = bytearray([0xfe, self.pid/255, self.pid%255, 0x01, (~(self.pid/255))&0xff, (~(self.pid%255))&0xff, 0x0c, 0x32, 0x05, 0x00, 0x00, 0x43])
				writebytes = ser.write( data)
				print("right stop")
				ser.close()

	def take_doll(self):
		with serial.Serial("/dev/ttyAMA0", 115200, timeout=1) as ser:	
			self.rand_pid()
			data = bytearray([0xfe, self.pid/255, self.pid%255, 0x01, (~(self.pid/255))&0xff, (~(self.pid%255))&0xff, 0x0c, 0x32, 0x04, 0x00, 0x00, 0x42])
			writebytes = ser.write( data)
			self.take_time = 10000
			print("take doll")
			ser.close()
			time.sleep(0.1)

	def loop(self):		
		if self.take_time > 0:
			self.take_time -= 20
			if self.take_time <= 0:
				print("take doll signal")

		data = []
		while self.ser.in_waiting > 0:
			data += ser.read(1)

		if len(data):
			print("parse receive data : \n\t")
			print(data)