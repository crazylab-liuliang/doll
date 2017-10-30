import RPi.GPIO as GPIO
import time

print(GPIO.VERSION)

GPIO.setmode(GPIO.BCM)

GPIO.setup( 2, GPIO.OUT)

while True:
	GPIO.output(2, GPIO.HIGH)
	time.sleep(5)
	GPIO.output(2, GPIO.LOW)
	time.sleep(1)
