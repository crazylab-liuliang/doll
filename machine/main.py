import camera
import network
import time
import machine
import threading
import RPi.GPIO as GPIO
import protocol.pb_machine_control as pb_mc
import protocol.pb_machine_login as pb_l

cm = camera.live_camera()
dm = machine.dollmachine()
nw = network.network()

def init():
	nw.connect_server("118.190.156.61", 8800)
	nw.login()
	nw.bind(pb_mc.machine_control(), dm.on_recv_machine_control)
	cm.begin_push_video_stream_0()
	#cm.begin_push_video_stream_1()

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

# init
init()

# net thread
t1 = threading.Thread(target=network_recv)
t1.setDaemon(True)
t1.start()

loop()
