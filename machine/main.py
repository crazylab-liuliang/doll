import camera
import network
import time
import machine
import threading
import RPi.GPIO as GPIO
import protocol.pb_machine_control as pb_mc
import protocol.pb_machine_login as pb_l

dm = machine.dollmachine()
nw = network.network()

def init():
	#camera.begin_push_video_stream_0()
	nw.connect_server("10.237.24.45", 8800)
	nw.login()
	nw.bind(pb_mc.machine_control(), dm.on_recv_machine_control)

def network_recv():
	print("netwrok recv...")
	while True:
		nw.recv()
		time.sleep(0.02)

def loop():
	print("main game loop...")
	while True:
		nw.process_net_bytes()
		dm.loop()
		time.sleep(0.02)

# run
init()

# net thread
t1 = threading.Thread(target=network_recv)
t1.start()

loop()
