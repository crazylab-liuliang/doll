import os
import socket
import protocol.pb_machine_login as pb

class network:
	sock = None

	def connect_server(self, host, port):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((host, port))
		print("connect server")

	def login(self):
		msg = pb.machine_login()
		msg.send(self.sock)
		print("login")

	def close(self):
		sock.close()

	def loop(self):
		if self.sock!=None:
			print("xxx")
			data = self.sock.recv(1024)
			print(data)
			if data:
				print("move left")
				print(data)
		else:
			print("b")