import socket

def Main():
	host = 'localhost'
	port = 5000

	s = socket.socket()
	s.connect(host, port)

	message = raw_input('-> ')
	while message != 'q':
		s.send(message)

		data = s.recv(1024)
		
