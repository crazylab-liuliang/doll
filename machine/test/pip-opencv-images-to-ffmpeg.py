import cv2
import subprocess as sp

output_file = 'rtmp://118.190.156.61:1935/live/apple'

cap = cv2.VideoCapture(0)


ret, frame = cap.read()
height, width, ch = frame.shape

ffmpeg = 'ffmpeg'
dimension = '{}x{}'.format(width, height)
f_format = 'bgr24' #remember OpenCV uses bgr format
fps = str(15)#str(cap.get(cv2.CAP_PROP_FPS))

command = [ffmpeg, '-f', 'rawvideo', '-s', dimension, '-pix_fmt', 'bgr24', '-f', 'flv', output_file]

#command = [ffmpeg, '-y', '-f', 'rawvideo', '-s', dimension, '-pix_fmt', 'bgr24', '-r', '30', '-i', '-', '-an', '-f', 'avi', '-r', '30', output_file]

proc = sp.Popen(command, stdin=sp.PIPE)

while True:
	ret, frame = cap.read()
	if not ret:
		break

	proc.stdin.write(frame.tostring())

cap.release()
