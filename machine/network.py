import os
import socket
import protocol.pb.machine_login

client_socket = None

def connect_server( host, port):
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect(host, port)
	print("connect server")

def login():
	msg = machine_login()
	msg.send(client_socket)
	print("login")

def close():
	client_socket.close()
