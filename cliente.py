from socket import *
import json

serverName = "localhost"
serverPort = 8000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

data = {}

option = str(input("Digite uma opção!\n"))
data["option"] = option

while option != "sair":
	clientSocket.send(json.dumps(data).encode('utf8'))
	retorno = clientSocket.recv(1024)
	print(retorno)
	option = str(input("Digite uma opção!\n"))
	data["option"] = option
clientSocket.close()
