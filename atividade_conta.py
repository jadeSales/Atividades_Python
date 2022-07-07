# Programação Orientada a Objetos
# Implementação de classes



class Conta:

	def __init__(self, titular, agencia, numero, saldo_inicial):
		self.__titular = titular
		self.__agencia = agencia
		self.__numero = numero
		self.__saldo = saldo_inicial
		self.__ativa = False
		self.__operacoes = [('saldo inicial', saldo_inicial)]
		pass


	@property
	def titular(self):
		return self.__titular
		pass


	@property
	def agencia(self):
		return self.__agencia
		pass
	

	@property
	def numero(self):
		return self.__numero
		pass
	

	@property
	def saldo(self):
		return self.__saldo
		pass
	

	@property
	def ativa(self):
		return self.__ativa
		pass
	

	@ativa.setter
	def ativa(self, situacao):
		if isinstance(situacao, bool):
			self.__ativa = situacao
		pass
	

	def depositar(self, valor):
		if self.__ativa == True and valor > 0:
			self.__saldo += valor
			self.__operacoes.append(('deposito', valor))
		pass


	def sacar(self, valor):
		if self.__ativa == True and valor > 0 and valor <= self.__saldo:
			self.__saldo -= valor
			self.__operacoes.append(('saque', valor))
		pass
		


	def transferir(self, conta_destino, valor):
		if self.__ativa == True and conta_destino.__ativa == True and valor > 0 and valor <= self.__saldo:
			self.__saldo -= valor
			conta_destino.depositar(valor)
			self.__operacoes.append(('transferencia', valor))
		pass
	

	def tirar_extrato(self):
		return self.__operacoes
		pass


