import RPi.GPIO as GPIO
import protocol.pb_machine_control as pb_mc

class dollmachine:

	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup( 2, GPIO.OUT)

	def __del__(self):
		self.cleanup()
	
	def on_recv_machine_control(self, msg):
		if msg.type==1:
			self.set_forward(msg.op)


	def set_forward(self, value):
		if value!=0:
			GPIO.output(2, GPIO.HIGH)
			print("forward begin")
		else:
			print("forward stop")
			GPIO.output(2, GPIO.LOW)

	def cleanup(self):
		GPIO.cleanup()
