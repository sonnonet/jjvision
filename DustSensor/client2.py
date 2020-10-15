import socket

HOST = socket.gethostname()
PORT = 50000
ADDR = (HOST, PORT)
BUFF_SIZE = 1024

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(ADDR)

with open('serverFile', 'wb') as f:
    print ('file opened')
    while True:
        print('receiving data...')
        data = clientSocket.recv(BUFF_SIZE)
        print('(data)', data)
        if not data:
            f.close()
            print ('file close')
            break
        f.write(data)

print('Successfully get the file')
clientSocket.close()
print('connection closed')
