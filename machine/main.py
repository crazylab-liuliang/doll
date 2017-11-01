import camera
import network
import time
import machine
import protocol.pb_machine_control as pb_mc
import protocol.pb_machine_login as pb_l

dm = machine.dollmachine()

#camera.begin_push_video_stream_0()
nw = network.network()
nw.connect_server("localhost", 8800)
nw.login()
nw.bind(pb_mc.machine_control(), on_recv_machine_control)
nw.loop()

# control from player
def on_recv_machine_control( msg):
	if msg.type==1:
		dm.set_forward(msg.op)