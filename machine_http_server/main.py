import camera
import network
import time
import machine
import threading
import RPi.GPIO as GPIO
import protocol.pb_machine_control as pb_mc
import protocol.pb_machine_login as pb_l
from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='templates')
cm = camera.live_camera()
dm = machine.dollmachine()
nw = network.network()

def init():
	nw.bind(pb_mc.machine_control(), dm.on_recv_machine_control)
	cm.begin_push_video_stream_0()

def network_recv():
	print("run flask...")
	app.debug = True
	app.run()

	time.sleep(0.02)

def loop():
	print("main game loop...")
	while True:
		nw.process_net_bytes()
		dm.loop()
		time.sleep(0.02)


@app.route('/op', methods=['GET', 'POST'])
def machine_op(self):
	op = request.args.get('op')
	code = request.args.get('code')
	nw.machine_op(op, code)

	return 1

# init
init()

# net thread
t1 = threading.Thread(target=network_recv)
t1.setDaemon(True)
t1.start()

loop()
