import serial
import RPi.GPIO as GPIO
import protocol.pb_machine_control as pb_mc


class dollmachine:
	ser = None
	coin_time = 0
	take_time = 0

	def __init__(self):
		self.ser = serial.Serial("/dev/ttyAMA0")
		#GPIO.setmode(GPIO.BCM)

	def __del__(self):
		self.ser.close()
		self.cleanup()

	def cleanup(self):
		GPIO.cleanup()

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
		data = [0xfe, 0x00, 0x00, 0x01, 0xff, 0xff, 0x10, 0x31, 0x3d, 0x01, 0x01, 0x01, 0x01, 0x01, 0x00, 0x1f]
		self.ser.write( data)
		self.coin_time = 200
		print("add coin - coin time [%d]" % self.coin_time)

	def set_forward(self, value):
		if value!=0:
			#GPIO.output(3, GPIO.HIGH)
			print("forward begin")
		else:
			print("forward stop")
			#GPIO.output(3, GPIO.LOW)

	def set_back(self, value):
		if value!=0:
			#GPIO.output(4, GPIO.HIGH)
			print("forward begin")
		else:
			print("forward stop")
			#GPIO.output(4, GPIO.LOW)


	def set_left(self, value):
		if value!=0:
			#GPIO.output(17, GPIO.HIGH)
			print("forward begin")
		else:
			print("forward stop")
			#GPIO.output(17, GPIO.LOW)

	def set_right(self, value):
		if value!=0:
			#GPIO.output(27, GPIO.HIGH)
			print("forward begin")
		else:
			print("forward stop")
			#GPIO.output(27, GPIO.LOW)

	def take_doll(self):
			#GPIO.output(22, GPIO.HIGH)
			self.take_time = 200

	def loop(self):
		if self.coin_time > 0:
			self.coin_time -= 20
			if self.coin_time <= 0:
				print("add coin signal")
				#GPIO.output(2, GPIO.LOW)

		if self.take_time > 0:
			self.take_time -= 20
			if self.take_time <= 0:
				print("take doll signal")
				#GPIO.output(22, GPIO.LOW)
