import socket
import threading

nickname = input("DIGITE SEU NICK: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def receive():
	while True:
		try:
			message = client.recv(1024).decode('ascii')
			if message == 'NICK':
				client.send(nickname.encode('ascii'))
			else:
				print(message)
		except:
			print("Erro")
			client.close()
			break
			
			
def write():
	while True:
		message = f'{nickname}: {input("")}'
		client.send(message.encode('ascii'))
		
receive_thread = threading.Thread(target=receive)
receive_thread.start()

while_thread = threading.Thread(target=write)
while_thread.start()
