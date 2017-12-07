import serial
import random
import RPi.GPIO as GPIO
import protocol.pb_machine_control as pb_mc


class dollmachine:
	ser = None
	coin_time = 0
	take_time = 0
	pid = 0

	def __init__(self):
		self.ser = serial.Serial("/dev/ttyAMA0", 115200, timeout=1.0)

	def __del__(self):
		self.ser.close()
		self.cleanup()

	def cleanup(self):
		return

	def rand_pid(self):
		self.pid = 0
		rd  = random.randint(0, 65535)
		while self.pid==rd:
			rd = random.randint(0, 65535)

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
			ser.flush()
			ser.close()
			self.coin_time = 200
			print("add coin - coin time [%d]" % self.coin_time)
			print("header --- [%d,%d,%d,%d]" % (data[1], data[2], data[4], data[5]))
			print("write bytes : %d" % writebytes )

			line = ser.readline()
			if len(line):
				print(line)


	def set_forward(self, value):
		if value!=0:
			self.rand_pid()
			data = bytearray([0xfe, self.pid/255, self.pid%255, 0x01, (~(self.pid/255))&0xff, (~(self.pid%255))&0xff, 0x0c, 0x32, 0x00, 0x00, 0x14, 0x52])
			writebytes = self.ser.write( data)
			self.ser.flush()
			print("forward begin")
			print("header --- [%d,%d,%d,%d]" % (data[1], data[2], data[4], data[5]))
			print("write bytes : %d" % writebytes )
		else:
			print("forward stop")
			self.rand_pid()
			data = bytearray([0xfe, self.pid/255, self.pid%255, 0x01, (~(self.pid/255))&0xff, (~(self.pid%255))&0xff, 0x0c, 0x32, 0x05, 0x00, 0x00, 0x43])
			writebytes = self.ser.write( data)
			self.ser.flush()
			print("header --- [%d,%d,%d,%d]" % (data[1], data[2], data[4], data[5]))
			print("write bytes : %d" % writebytes )

	def set_back(self, value):
		if value!=0:
			self.rand_pid()
			data = bytearray([0xfe, self.pid/255, self.pid%255, 0x01, (~(self.pid/255))&0xff, (~(self.pid%255))&0xff, 0x0c, 0x32, 0x01, 0x00, 0x14, 0x53])
			writebytes = self.ser.write( data)
			self.ser.flush()
			print("back begin")
			print("header --- [%d,%d,%d,%d]" % (data[1], data[2], data[4], data[5]))
			print("write bytes : %d" % writebytes )
		else:
			print("back stop")
			self.rand_pid()
			data = bytearray([0xfe, self.pid/255, self.pid%255, 0x01, (~(self.pid/255))&0xff, (~(self.pid%255))&0xff, 0x0c, 0x32, 0x05, 0x00, 0x00, 0x43])
			writebytes = self.ser.write( data)
			self.ser.flush()
			print("header --- [%d,%d,%d,%d]" % (data[1], data[2], data[4], data[5]))
			print("write bytes : %d" % writebytes )


	def set_left(self, value):
		if value!=0:
			self.rand_pid()
			data = bytearray([0xfe, self.pid/255, self.pid%255, 0x01, (~(self.pid/255))&0xff, (~(self.pid%255))&0xff, 0x0c, 0x32, 0x02, 0x00, 0x14, 0x54])
			writebytes = self.ser.write( data)
			self.ser.flush()
			print("left begin")
			print("header --- [%d,%d,%d,%d]" % (data[1], data[2], data[4], data[5]))
			print("write bytes : %d" % writebytes )
		else:
			print("left stop")
			self.rand_pid()
			data = bytearray([0xfe, self.pid/255, self.pid%255, 0x01, (~(self.pid/255))&0xff, (~(self.pid%255))&0xff, 0x0c, 0x32, 0x05, 0x00, 0x00, 0x43])
			writebytes = self.ser.write( data)
			self.ser.flush()
			print("header --- [%d,%d,%d,%d]" % (data[1], data[2], data[4], data[5]))
			print("write bytes : %d" % writebytes )

	def set_right(self, value):
		if value!=0:
			self.rand_pid()
			data = bytearray([0xfe, self.pid/255, self.pid%255, 0x01, (~(self.pid/255))&0xff, (~(self.pid%255))&0xff, 0x0c, 0x32, 0x03, 0x00, 0x14, 0x55])
			writebytes = self.ser.write( data)
			self.ser.flush()
			print("right begin")
			print("header --- [%d,%d,%d,%d]" % (data[1], data[2], data[4], data[5]))
			print("write bytes : %d" % writebytes )
		else:
			self.rand_pid()
			data = bytearray([0xfe, self.pid/255, self.pid%255, 0x01, (~(self.pid/255))&0xff, (~(self.pid%255))&0xff, 0x0c, 0x32, 0x05, 0x00, 0x00, 0x43])
			writebytes = self.ser.write( data)
			self.ser.flush()
			print("right stop")
			print("header --- [%d,%d,%d,%d]" % (data[1], data[2], data[4], data[5]))
			print("write bytes : %d" % writebytes )

	def take_doll(self):
			self.rand_pid()
			data = bytearray([0xfe, self.pid/255, self.pid%255, 0x01, (~(self.pid/255))&0xff, (~(self.pid%255))&0xff, 0x0c, 0x32, 0x04, 0x00, 0x00, 0x42])
			writebytes = self.ser.write( data)
			self.ser.flush()
			self.take_time = 200
			print("take doll")
			print("header --- [%d,%d,%d,%d]" % (data[1], data[2], data[4], data[5]))
			print("write bytes : %d" % writebytes )

	def loop(self):
		if self.coin_time > 0:
			self.coin_time -= 20
			if self.coin_time <= 0:
				print("add coin signal")
				print("serial baudrate : %d" % self.ser.baudrate)

		if self.take_time > 0:
			self.take_time -= 20
			if self.take_time <= 0:
				print("take doll signal")
				print("serial baudrate : %d" % self.ser.baudrate)

		#line = self.ser.readline()
		#if len(line):
		#	print(line)
