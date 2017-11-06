import os
import subprocess

class live_camera:

	camera_process_0 = None

	def __del__(self):
		stop_push_video_stream_0()

	def begin_push_video_stream_0():
		camera_process_0 = subprocess.Popen(['ffmpeg', '-f', 'v4l2', '-framerate', '25', '-video_size', '640x480', '-i', '/dev/video0', '-f', 'mpegts', '-codec:v', 'mpeg1video', '-s', '640x480', '-b:v', '1000k', '-bf', '0', 'http://118.190.156.61:10001/secret'])
		print("begin push video stream 0")

	def stop_push_video_stream_0():
		if camera_process_0!=None:
			camera_process_0.terminate()
