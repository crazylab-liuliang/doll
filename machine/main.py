import camera
import network
import time
import machine
import RPi.GPIO as GPIO
import protocol.pb_machine_control as pb_mc
import protocol.pb_machine_login as pb_l

def run():
	dm = machine.dollmachine()

	#camera.begin_push_video_stream_0()
	nw = network.network()
	nw.connect_server("10.237.24.45", 8800)
	nw.login()
	nw.bind(pb_mc.machine_control(), dm.on_recv_machine_control)
	while True:
		nw.loop()

# run
run()
