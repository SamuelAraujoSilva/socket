from socket import *
import json

serverName = "localhost"
serverPort = 5000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

while True:
	option = str(input("Digite uma opção!\n"))
	if option == "sair":
		data = json.dumps({"option": str(option)})
		clientSocket.send(data.encode("ascii"))
		retorno = clientSocket.recv(1024)
		print(retorno)
		break
	elif option == "criar":
		nome = str(input("Digite o nome: \n"))
		data = json.dumps({"option": str(option), "nome": nome})
		clientSocket.send(data.encode("ascii"))
	elif option == "info":
		data = json.dumps({"option": str(option)})
		clientSocket.send(data.encode("ascii"))
		retorno = clientSocket.recv(1024)
		print(retorno)
	elif option == "buscar":
		data = json.dumps({"option": str(option)})
		clientSocket.send(data.encode("ascii"))
		retorno = clientSocket.recv(1024)
		print(retorno)
	elif option == "atacar":
		data = json.dumps({"option": str(option)})
		clientSocket.send(data.encode("ascii"))
		retorno = clientSocket.recv(1024)
		print(retorno)
	elif option == "ignorar":
		data = json.dumps({"option": str(option)})
		clientSocket.send(data.encode("ascii"))
		retorno = clientSocket.recv(1024)
		print(retorno)
	else:
		print("opção invalida!")
	clientSocket.close()


# while True:
# 	menu = int(input("Escolhar uma opção\n"
# 					 "1 - Liste Meus Compromissos\n"
# 					 "2 - Adicionar novo compromisso\n"
# 					 "3 - Atualizar compromisso\n"))
#
# 	data = None
#
# 	if menu == 1:
# 		data = json.dumps({"ACTION": "LIST"})
# 	elif menu == 2:
# 		novo_compromisso = input("Digite seu compromisso: \n")
# 		data = json.dumps({"ACTION": "CREATE", "ITEM": novo_compromisso})
# 	elif menu == 3:
# 		data = json.dumps({"ACTION": "UPDATE", "ITEM": novo_compromisso})
# 	else:
# 		print("Opção invalida!")
#
# 	if data:
# 		clientSocket.send(data.encode("ascii"))
# 		retorno = clientSocket.recv(1024)
# 		print(retorno)

# while True:
# 	opcao = input("Digite a opção: ")
# 	if opcao == "LIST":
# 		clientSocket.send(json.dumps({"ACTION": "LIST"}).encode("ascii"))
# 	elif opcao == "CREATE":
# 		compromisso = input("Digite o compromisso: ")
# 		clientSocket.send(json.dumps({"ACTION": "CREATE", "ITEM": compromisso}).encode("ascii"))
# 	else:
# 		print("Opção invalida!")
#
# 	retorno = clientSocket.recv(1024)
# 	print(retorno)

# clientSocket.close()
