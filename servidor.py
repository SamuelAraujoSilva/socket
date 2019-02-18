from socket import *
import _thread
import random
import json

serverPort = 5000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

agendas = {}

# def task(connection, client):
# 	agenda_name = "agenda_{}".format(client[1])
# 	if not agenda_name in agendas:
# 		agendas[agenda_name] = []
# 	while True:
# 		received = connection.recv(1024)
# 		if received:
# 			data = json.loads(received)
# 			if data["ACTION"] == "CREATE":
# 				agendas[agenda_name].append(data["ITEM"])
# 				if data["ITEM"] in agendas[agenda_name]:
# 					retorno = {"CODIGO": 200, "MESSAGE": "Item adicionado com sucesso"}
# 					connection.send(json.dumps(retorno).encode("ascii"))
# 				else:
# 					retorno = {"CODIGO": 400, "MESSAGE": "Falha ao adicionar item"}
# 					connection.send(json.dumps(retorno).encode("ascii"))
# 			if data["ACTION"] == "UPDATE":
# 				print(agendas[agenda_name][data["ITEM"]])
# 				retorno = {"CODIGO": 200, "MESSAGE": "Item atualizado com sucesso"}
# 				connection.send(json.dumps(retorno).encode("ascii"))
# 				# for i, item in enumerate(agendas[agenda_name]):
# 				# 	if item.id == data["ITEM"]["id"]:
# 				# 		agendas[agenda_name][i] = data["ITEM"]
# 				# if data["ITEM"] in agendas[agenda_name]:
# 				# 	retorno = {"CODIGO": 200, "MESSAGE": "Item atualizado com sucesso"}
# 				# 	connection.send(json.dumps(retorno).encode("ascii"))
# 				# else:
# 				# 	retorno = {"CODIGO": 400, "MESSAGE": "Falha ao atualizar item"}
# 				# 	connection.send(json.dumps(retorno).encode("ascii"))
# 			if data["ACTION"] == "LIST":
# 				if len(agendas[agenda_name]) == 0:
# 					retorno = {"CODIGO": 200, "MESSAGE": "Agenda vazia!"}
# 					connection.send(json.dumps(retorno).encode("ascii"))
# 				else:
# 					connection.send(json.dumps(agendas[agenda_name]).encode("ascii"))
# 			if data["ACTION"] == "DELETE":
# 				for i, item in enumerate(agendas[agenda_name]):
# 					if item.id == data["ID"]:
# 						agendas[agenda_name].pop(i)
# 				if not data["ITEM"] in agendas[agenda_name]:
# 					retorno = {"CODIGO": 200, "MESSAGE": "Item removido com sucesso"}
# 					connection.send(json.dumps(retorno).encode("ascii"))
# 				else:
# 					retorno = {"CODIGO": 400, "MESSAGE": "Falha ao remover item"}
# 					connection.send(json.dumps(retorno).encode("ascii"))
# 	connection.close()

class Personagem():
	def __init__(self, nome):
		self.nome = nome
		self.nivel = 1
		self.vida = 100
		self.ataque = 10

	def subil_nivel(self):
		self.nivel += 1
		self.vida += 100
		self.ataque += 5

class Monstro():
	def __init__(self):
		self.nivel = random.randint(0, 5)
		self.vida = self.nivel*50
		self.ataque = self.nivel*5

	def atacado(self, ataque):
		self.vida -= ataque

def task(connection, client):
	personagem = None
	monstro = None
	received = json.loads(connection.recv(1024))
	while received["option"] != "sair":
		if received["option"] == "criar":
			if not personagem:
				nome = received["nome"]
				personagem = Personagem(nome)
				data = {"status": 200, "messagem": "Personagem criado com sucesso!"}
			else:
				data = {"status": 401, "messagem": "Você ja possui um personagem!"}
			connection.send(json.dumps(data).encode("ascii"))
		elif received["option"] == "info":
			if not personagem:
				data = {"status": 400, "message": "Você ainda ñ criou um personagem"}
			else:
				data = {"status": 200, "personagem": {"nome": personagem.nome, "nivel": personagem.nivel, "vida": personagem.vida, "ataque": personagem.ataque}}
			connection.send(json.dumps(data).encode("ascii"))
		elif received["option"] == "buscar":
			if not monstro:
				monstro = Monstro()
			data = {"status": 200, "monstro": {"nivel": monstro.nivel, "vida": monstro.vida, "ataque": monstro.ataque}}
			connection.send(json.dumps(data).encode("ascii"))
		elif received["option"] == "atacar":
			if personagem:
				if monstro:
					monstro.atacado(personagem.ataque)
					if monstro.vida <= 0:
						data = {"status": 200, "messagem": "monstro Morreu"}
						monstro = None
						personagem.subil_nivel()
					else:
						data = {"status": 200, "messagem": "monstro foi atacado.", "monstro": {"nivel": monstro.nivel, "vida": monstro.vida, "ataque": monstro.ataque}}
				else:
					data = {"status": 400, "messagem": "Nenhuma monstro a vista. Faça uma busca antes de atacar"}
			else:
				data = {"status": 400, "messagem": "Você ainda ñ criou um personagem"}
			connection.send(json.dumps(data).encode("ascii"))
		elif received["option"] == "ignorar":
			if not personagem:
				data = {"status": 400, "messagem": "Você ainda ñ criou um personagem"}
			else:
				if not monstro:
					data = {"status": 400, "messagem": "Nenhuma monstro a vista. Faça uma busca antes de atacar"}
				else:
					monstro = None
					data = {"status": 200, "messagem": "Monstro muito forte! vamos para o proximo"}
			connection.send(json.dumps(data).encode("ascii"))
		else:
			data = {"error": 400, "messagem": "opção invalida!"}
			connection.send(json.dumps(data).encode("ascii"))
		received = json.loads(connection.recv(1024))
	data = {"message": "Ate mais!"}
	connection.send(json.dumps(data).encode("ascii"))
	print("cliente {} saiu".format(client[1]) )
	connection.close()

print ("O servidor está pronto para receber!")
while 1:
	connection, addr = serverSocket.accept()
	_thread.start_new_thread(task, (connection, addr))
	
	
	
	
