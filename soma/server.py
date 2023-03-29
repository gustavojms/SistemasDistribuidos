import socket

serverIp = "0.0.0.0"
serverPort = 46000
serverEndPoint = (serverIp, serverPort)
bufferSize = 1024

serverSocketTcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocketTcp.bind(serverEndPoint)
serverSocketTcp.listen(5)

while True:
    clientConnection, clientAddress = serverSocketTcp.accept()
    
    clientData = clientConnection.recv(bufferSize)
    
    if not clientData:
        break
    
    n1, n2 = str(clientData, 'ascii').split(',')
    soma = int(n1) + int(n2)
    print("Os numeros sao: {}".format(clientData))
    
    response = "A soma e: {}".format(soma)
    dataFormated = str.encode(response)
    
    clientConnection.send(dataFormated)
    
    clientConnection.close()
    