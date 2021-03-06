import serial
import time
import random


class dollmachine:
	ser = None
	take_time = 0
	loop_time = 0.0
	pid = 0

	def __init__(self):
		self.ser = serial.Serial("/dev/ttyAMA0", 115200, timeout=10, stopbits=serial.STOPBITS_TWO, rtscts=True, dsrdtr=True)
		return

	def __del__(self):
		self.cleanup()

	def cleanup(self):
		if self.ser != None:
			self.ser.close()

		if self.ser_rcv != None and self.ser_rcv.is_open:
			self.ser_rcv.close()

		return

	def reopen_ser(self):
		return

	def rand_pid(self):
		self.pid = 0
		rd  = random.randint(0, 65025)
		while self.pid==rd:
			rd = random.randint(0, 65025)

		self.pid = rd
		self.reopen_ser()

	def on_recv_machine_control(self, type):
		print("on recv machine control [%d,%d]" % (msg.type, msg.op))
		if type==0:
			self.add_coin()

		if type==1:
			self.set_forward(msg.op)

		if type==2:
			self.set_back(msg.op)

		if type==3:
			self.set_left(msg.op)

		if type==4:
			self.set_right(msg.op)

		if type==5:
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
		time.sleep(0.1)


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
		self.take_time = 10000
		print("take doll")
		time.sleep(0.1)

	def loop(self, delta):
		while True:
			self.loop_time += delta
			if self.loop_time > 5:
				# send data
				rd  = random.randint(0, 5)
				self.on_recv_machine_control(rd)

				# recieve data
				data = []
				inbuff = self.ser.in_waiting
				while inbuff > 0:
					data += self.ser.read(inbuff)
					inbuff = self.ser.in_waiting

				if len(data):
					print("parse receive data : \n\t")
					print(data)
				
				self.loop_time =0.0


dm = dollmachine()
dm.loop()