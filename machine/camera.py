import os
import subprocess

camera_push_video_stream_0_process = None

def begin_push_video_stream_0():
	camera_push_video_stream_0_process = subprocess.Popen(["avconv", "-f", "video4linux2", "-r", "25", "-i", "/dev/video0", "-f", "flv", "rtmp://118.190.156.61/live/test"])
	print("begin push video stream 0")

def stop_push_video_stream_0():
	if camera_push_video_stream_0_process!=None:
		camera_push_video_stream_0_process.terminate()

def begin_push_video_stream_1():
	subprocess.Popen(["avconv", "-f", "video4linux2", "-r", "25", "-i", "/dev/video1", "-f", "flv", "rtmp://118.190.156.61/live/test"])
	print("begin push video stream 1")
