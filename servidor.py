from socket import *
import _thread
import random
import json

serverPort = 11600
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)


def task(connection, client):
	agenda = []
	while True:
		received = connection.recv(1024)
		if received:
			data = json.loads(received)
			if data["ACTION"] == "CREATE":
				agenda.append(data["ITEM"])
				if data["ITEM"] in agenda:
					retorno = {"CODIGO": 200, "MESSAGE": "Item adicionado com sucesso"}
					connection.send(json.dumps(retorno).encode("ascii"))
				else:
					retorno = {"CODIGO": 400, "MESSAGE": "Falha ao adicionar item"}
					connection.send(json.dumps(retorno).encode("ascii"))
			if data["ACTION"] == "UPDATE":
				for i, item in enumerate(agenda):
					if item.id == data["ID"]:
						agenda[i] = data["ITEM"]
				if data["ITEM"] in agenda:
					retorno = {"CODIGO": 200, "MESSAGE": "Item atualizado com sucesso"}
					connection.send(json.dumps(retorno).encode("ascii"))
				else:
					retorno = {"CODIGO": 400, "MESSAGE": "Falha ao atualizar item"}
					connection.send(json.dumps(retorno).encode("ascii"))
			if data["ACTION"] == "LIST":
				if len(agenda) == 0:
					retorno = {"CODIGO": 200, "MESSAGE": "Agenda vazia!"}
					connection.send(json.dumps(retorno).encode("ascii"))
				else:
					connection.send(json.dumps(agenda).encode("ascii"))
			if data["ACTION"] == "DELETE":
				for i, item in enumerate(agenda):
					if item.id == data["ID"]:
						agenda.pop(i)
				if not data["ITEM"] in agenda:
					retorno = {"CODIGO": 200, "MESSAGE": "Item removido com sucesso"}
					connection.send(json.dumps(retorno).encode("ascii"))
				else:
					retorno = {"CODIGO": 400, "MESSAGE": "Falha ao remover item"}
					connection.send(json.dumps(retorno).encode("ascii"))
	connection.close()

print ("The server is ready to receive")
while 1:
	connection, addr = serverSocket.accept()
	_thread.start_new_thread(task, (connection, addr))
	
	
	
	
