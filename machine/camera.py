import os
import subprocess

class live_camera:

	camera_process_0 = None
	camera_process_1 = None

	def __del__(self):
		self.stop_push_video_stream_0()
		self.stop_push_video_stream_1()

	def begin_push_video_stream_0(self):
		self.camera_process_0 = subprocess.Popen(['ffmpeg', '-f', 'v4l2', '-framerate', '25', '-video_size', '320x240', '-i', '/dev/video0', '-f', 'mpegts', '-codec:v', 'mpeg1video', '-s', '320x240', '-b:v', '1000k', '-bf', '0', 'http://118.190.156.61:10001/camera_0'])
		print("begin push video stream 0")

	def stop_push_video_stream_0(self):
		if self.camera_process_0!=None:
			self.camera_process_0.terminate()

	def begin_push_video_stream_1(self):
		self.camera_process_1 = subprocess.Popen(['ffmpeg', '-f', 'v4l2', '-framerate', '25', '-video_size', '320x240', '-i', '/dev/video1', '-f', 'mpegts', '-codec:v', 'mpeg1video', '-s', '320x240', '-b:v', '1000k', '-bf', '0', 'http://118.190.156.61:10001/camera_1'])
		print("begin push video stream 1")

	def stop_push_video_stream_1(self):
		if self.camera_process_1!=None:
			self.camera_process_1.terminate()
