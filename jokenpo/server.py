import socket
import threading
import time

moves = {'rock': 0, 'paper': 1, 'scissors': 2}
players = []
playerMove = [None, None]

def handleConnection(conn, playerNumber):
    print(f'Player {playerNumber} connected')
    while True:
        data = conn.recv(1024)
        if not data:
            break
        move = data.decode('utf-8')
        playerMove[playerNumber] = move

def handleResults(playerMove):
    result = ''
    if playerMove[0] == playerMove[1]:
        result = 'Its a draw'
    elif (int(playerMove[0]) - int(playerMove[1])) % 3 == 1:
        result = 'Player 1 wins'
    else:
        result = 'Player 2 wins'
    return result

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 46000))
sock.listen(2)

playerNumber = 0
while len(players) < 2:
    conn, addr = sock.accept()
    players.append(conn)
    print(f'Player {playerNumber} connected')
    threading.Thread(target=handleConnection, args=(conn, playerNumber)).start()
    playerNumber += 1

while True:
    if playerMove[0] is None or playerMove[1] is None:
        time.sleep(0.1)
        continue
    handleResults(playerMove)

    for player in players:
        player.send(bytes(f'Winner: {playerNumber}', 'utf-8'))
    playerMove = [None, None]
