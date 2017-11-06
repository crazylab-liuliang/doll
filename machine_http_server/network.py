import os
import socket
import struct
import threading
import protocol.pb_machine_control as pb_mc
import protocol.pb_machine_login as pb_l

class network:
	sock = None
	msg_bind = []
	net_data = bytes()
	net_data_lock = threading.Lock()
	data_buffer = bytes()
	header_size = 8
	tail_size = 2

	def connect_server(self, host, port):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((host, port))
		print("connect server")

	def login(self):
		msg = pb_l.machine_login()
		msg.send(self.sock)
		print("login")

	def close(self):
		sock.close()

	def recv(self):
		if self.sock!=None:
			data = self.sock.recv(1024)
			if data:
				self.net_data_lock.acquire()
				self.net_data += data
				self.net_data_lock.release()
			else:
				print("socket is None")

	
	def process_net_bytes(self):
		if True:
			self.net_data_lock.acquire()
			self.data_buffer += self.net_data
			self.net_data = bytes()
			self.net_data_lock.release()

			if len(self.data_buffer) < self.header_size:
				return

			# read net package header
			head_pack = struct.unpack('!ii', self.data_buffer[:self.header_size])
			body_size = head_pack[1]

			if len(self.data_buffer) < self.header_size + body_size + self.tail_size:
				return

			body_pack = self.data_buffer[self.header_size : self.header_size+body_size]
			self.process_net_pack(head_pack, body_pack)

			self.data_buffer = self.data_buffer[self.header_size+body_size+self.tail_size:]

	def process_net_pack(self, head, body):	
		msg_id = head[0]
		msg_size = head[1]

		print(msg_id)

		if msg_id < len(self.msg_bind):
			msg = self.msg_bind[msg_id][0]
			msg_cb = self.msg_bind[msg_id][1]
			msg.parse_data(body)
			msg_cb(msg)

	def bind(self, msg, func):
		msg_id = msg.id()
		while msg_id+1 > len(self.msg_bind):
			self.msg_bind.append(None)

		self.msg_bind[msg_id] = [msg, func]