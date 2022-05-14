import socket
import json
import time
import pickle

socket = socket.socket()
socket.bind(('', 12341))
socket.listen(2)
connect, addr = socket.accept()
connect1, addr1 = socket.accept()

print(f'''
Клиент 1
ip: {addr}

Клиент 2
ip: {addr1}
''')


game_data = {
    'snake_pside': '',
    'snake1_pside': '',
    'apple_coords': '',

}

while True:
    data = connect.recv(1024)
    if not data:
        break
    data = pickle.loads(data)

    if data.get('host'):
        data_for_client = data
    else:
        data_for_host = data






    data = connect1.recv(1024)
    if not data:
        break
    data = pickle.loads(data)

    if data.get('host'):
        data_for_client = data
    else:
        data_for_host = data


    connect.send(pickle.dumps(data_for_host))
    connect1.send(pickle.dumps(data_for_client))





