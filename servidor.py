from socket import *
import _thread
import random
import json

serverPort = 8000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

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
				personagem = Personagem(client[1])
				data = {"status": 200, "messagem": "Personagem criado com sucesso!"}
			else:
				data = {"status": 400, "messagem": "Você ja possui um personagem!"}
		elif received["option"] == "info":
			if not personagem:
				data = {"status": 400, "message": "Você ainda ñ criou um personagem"}
			else:
				data = {"status": 200, "personagem": {"nome": personagem.nome, "nivel": personagem.nivel, "vida": personagem.vida, "ataque": personagem.ataque}}
		elif received["option"] == "buscar":
			if not monstro:
				monstro = Monstro()
			data = {"status": 200, "monstro": {"nivel": monstro.nivel, "vida": monstro.vida, "ataque": monstro.ataque}}
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
		elif received["option"] == "ignorar":
			if not personagem:
				data = {"status": 400, "messagem": "Você ainda ñ criou um personagem"}
			else:
				if not monstro:
					data = {"status": 400, "messagem": "Nenhuma monstro a vista. Faça uma busca antes de atacar"}
				else:
					monstro = None
					data = {"status": 200, "messagem": "Monstro muito forte! vamos para o proximo"}
		else:
			data = {"error": 400, "messagem": "opção invalida!"}
		connection.send(json.dumps(data).encode("utf8"))
		received = json.loads(connection.recv(1024))
	print("{} saiu".format(client[1]))
	connection.close()

print ("O servidor está pronto para receber!")
while 1:
	connection, addr = serverSocket.accept()
	_thread.start_new_thread(task, (connection, addr))
	
	
	
	
