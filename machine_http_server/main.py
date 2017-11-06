import camera
import network
import time
import machine
import threading
import RPi.GPIO as GPIO
import protocol.pb_machine_control as pb_mc
import protocol.pb_machine_login as pb_l
from flask import Flask
from flask import request

app = Flask(__name__, static_url_path='', static_folder='templates')
cm = camera.live_camera()
dm = machine.dollmachine()
nw = network.network()

def init():
	nw.bind(pb_mc.machine_control(), dm.on_recv_machine_control)
	#cm.begin_push_video_stream_0()

def start_flask_server():
	print("run flask server...")
	app.debug = True
	app.run(port=80)

	time.sleep(0.02)

def loop():
	print("main game loop...")
	while True:
		nw.process_net_bytes()
		dm.loop()
		time.sleep(0.02)


@app.route('/op', methods=['GET', 'POST'])
def machine_op():
	op = request.args.get('op')
	code = request.args.get('code')
	nw.machine_op(op, code)

	return 1

# init
init()

# net thread
t1 = threading.Thread(target=loop)
t1.setDaemon(True)
t1.start()

start_flask_server()
