import numpy as np
import cv2
import time
import subprocess as sp

cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)

idx  = 0
time_elapsed = 0

command = ['ffmpeg',
	'-y',
	'-f', 'rawvideo',
	'-vcodec', 'rawvideo',
	'-pix_fmt', 'bgr24',
	'-s', '480x320',
	'-i', '-',
	'-c:v', 'libx264',
	'-pix_fmt', 'yuv420p',
	'-preset', 'ultrafast',
	'-f', 'flv',
	'rtmp://118.190.156.61/live/machine_0']

proc = sp.Popen(command, stdin=sp.PIPE, shell = False)


while(True):

	time.sleep(0.1)
	time_elapsed = time_elapsed+1
	if time_elapsed > 50:
		idx = (idx+1) % 2
		time_elapsed = 0

	
	if time_elapsed==0:#idx==0:
		# capture frame by frame
		ret, frame = cap0.read()

		# Ouroperations on the frame come here
		grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# Display the resulting frame
		#cv2.imshow('frame', grey)

		print(grey)

		#proc.stdin.write(frame.tostring())

	else:
		# capture frame by frame
		ret, frame = cap1.read()

		# Ouroperations on the frame come here
		grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# Display the resulting frame
		#cv2.imshow('frame', grey)

		#proc.stdin.write(frame.tostring())


	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
