from http import server
import socket

serverIp = "10.35.4.52"
serverPort = 1234
serverEndPoint = (serverIp, serverPort)
bufferSize = 1024

clientSocketTcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocketTcp.connect(serverEndPoint)

clientSocketTcp.send(b'Gustavo Jose e Antonio Pedro')
dataServer = clientSocketTcp.recv(bufferSize)

print("Mensagem do servidor: {}".format(dataServer))

clientSocketTcp.close()