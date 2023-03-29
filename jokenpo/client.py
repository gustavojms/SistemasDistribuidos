import socket

sock = socket.socket()
sock.connect(('localhost', 46000))

while True:
    move = input('rock{0}, paper{1} or scissors{2}? ')
    sock.send(bytes(move, 'utf-8'))
    data = sock.recv(1024)
    print(data.decode('utf-8'))

sock.close()