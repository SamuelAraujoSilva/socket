from socket import *
import json

serverName = "localhost"
serverPort = 11600
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

# data = json.dumps({"ACTION": "CREATE", "ITEM": {"compromisso": "teste"}})
# print(data)
# clientSocket.send(data.encode("ascii"))
# retorno = clientSocket.recv(1024)
# print(retorno)
#
# data = json.dumps({"ACTION": "LIST"})
# clientSocket.send(data.encode("ascii"))
# retorno = clientSocket.recv(1024)
# print(retorno)


while True:
	Menu = input("Escolhar uma opção\n"
				 "1 - Liste Meus Compromissos\n"
				 "2 - Adicionar novo compromisso\n"
				 "3 - Atualizar compromisso")

# clientSocket.close()
