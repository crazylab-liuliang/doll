import os
import socket
import protocol.pb_machine_login as pb

class network:
	sock = None

	def connect_server(self, host, port):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((host, port))
		print("connect server")
		print(self.sock)

	def login(self):
		msg = pb.machine_login()
		print("NM")
		print(self.sock)
		msg.send(self.sock)
		print("login")

	def close(self):
		sock.close()
