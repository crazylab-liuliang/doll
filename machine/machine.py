import RPi.GPIO as GPIO

class dollmachine:

	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup( 2, GPIO.OUT)

	def set_forward(self, value):
		if value!=0:
			GPIO.output(2, GPIO.HIGH)
			print("forward begin")
		else:
			print("forward stop")
			GPIO.output(2, GPIO.LOW)
