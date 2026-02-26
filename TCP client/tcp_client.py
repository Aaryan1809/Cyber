import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 5000))

client.send("Jay Swaminarayan".encode())

data = client.recv(1024)

print(data.decode())
