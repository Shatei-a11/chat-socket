import threading
import socket

host = '127.0.0.1'#localhost
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = [ ]
nicknames = [ ]

def broadcast(message):
	for client in clients:
		client.send(message)

def handle(client):
	while True:
		try:
			message = client.recv(1024)
			broadcast(message)
		except:
			index = client.index(client)
			clients.remove(client)
			client.close()
			nickname = nicknames[index]
			broadcast(f"{nickname} Saiu".encode('ascii'))
			nickname.remove(nickname)
			break
			
def receive():
	while True:
		client, address = server.accept()
		print(f"IP DO CONECTADO {str(address)}")
		
		client.send('NICK'.encode('ascii'))
		nickname = client.recv(1024).decode('ascii')
		nicknames.append(nickname)
		clients.append(client)
		
		print(f"O nick do cliente e {nickname}")
		broadcast(f'{nickname} Entrou'.encode('ascii'))
		
		thread = threading.Thread(target=handle, args=(client,))
		thread.start()
		
print("ESPERANDO ALGUEM ENTRAR...")
receive()
