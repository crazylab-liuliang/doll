import camera
import network
import time
import machine
import protocol.pb_machine_control as pb_mc
import protocol.pb_machine_login as pb_l

# control from player
def on_recv_machine_control( msg):
	if msg.type==1:
		dm.set_forward(msg.op)


dm = machine.dollmachine()

#camera.begin_push_video_stream_0()
nw = network.network()
nw.connect_server("10.237.24.45", 8800)
nw.login()
nw.bind(pb_mc.machine_control(), on_recv_machine_control)

while True:
	nw.loop()
