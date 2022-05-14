import socket
import json
import pickle

socket = socket.socket()
socket.connect(('localhost', 12341))

print('Подключение прошло успешно!')
data = {
    'biba': 'biba',
    'who': 'whOO'
}

while True:
    # message = input().encode('ascii')
    message = pickle.dumps(data)
    socket.send(message)
    data = socket.recv(1024)
    if not data:
        break
    data = pickle.loads(data)
    print(data)

socket.close()
