import camera
import network
import time

#camera.begin_push_video_stream_0()
nw = network.network()
nw.connect_server("localhost", 8800)
nw.login()

while True:
    nw.loop()
    time.sleep(0.1)