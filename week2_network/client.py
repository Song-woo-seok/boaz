from socket import *

serverName = '127.0.0.1'
serverPort = 13000

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))
print('connected')

sentence = input('Client Message: ')
clientSocket.send(sentence.encode())
print('send a Message')

modifiedSentence = clientSocket.recv(1024)
modifiedSentence = modifiedSentence.decode()
print('The clienti received: ', modifiedSentence)

clientSocket.close()
