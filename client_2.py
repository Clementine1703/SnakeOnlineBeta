import socket
import json

socket = socket.socket()
socket.connect(('localhost', 12341))

print('Подключение прошло успешно!')

while True:
    # message = input().encode('ascii')
    message = 'server 2'.encode('ascii')
    socket.send(message)
    data = socket.recv(1024)
    if not data:
        break
    print(data)

socket.close()
