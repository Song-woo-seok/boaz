from socket import *

ip = '127.0.0.1'
serverPort = 13000

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind((ip, serverPort))
serverSocket.listen(1)
print('The server is running')

connectionSocket, addr = serverSocket.accept()
print('connected')

data = connectionSocket.recv(1024)
sentence = data.decode()
print('The server received: ', sentence)

sendMessage = input('Server Message: ')
connectionSocket.send(sendMessage.encode())

connectionSocket.close()
