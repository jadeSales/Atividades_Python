# Programação Orientada a Objetos
# Implementação de classes, herança, polimorfismo e lançamento de exceções.
#


class Produto:

	def __init__(self, nome, preco):
		self.nome = nome
		self.preco = preco
		pass

	
	@property
	def nome(self):
		return self.__nome
		pass

	
	@property
	def preco(self):
		return self.__preco
		pass

	
	@nome.setter
	def nome(self, novo_nome):
		if len(str(novo_nome)) > 0:
			self.__nome = novo_nome
		else:
			raise ValueError
		pass

	
	@preco.setter
	def preco(self, novo_preco):
		if isinstance(novo_preco, int) or isinstance(novo_preco, float):
			if novo_preco >= 0:
				self.__preco = novo_preco
			else:
				raise ValueError
		else:
			raise TypeError
		pass

	
	def calcular_preco_com_frete(self):
		return self.__preco
		pass


class ProdutoFisico(Produto):

	def __init__(self, nome, preco, peso):
		super(ProdutoFisico, self).__init__(nome, preco)
		self.peso = peso
		pass
	

	@property
	def peso(self):
		return self.__peso
		pass
	

	@peso.setter
	def peso(self, novo_peso):
		if isinstance(novo_peso, int):
			if novo_peso <= 0: 
				raise ValueError
			else:
				self.__peso = novo_peso
		else:
			raise TypeError
		pass

	
	def peso_em_kg(self):
		self.__peso = self.__peso / 1000
		return self.__peso
		pass


	def calcular_preco_com_frete(self):
		frete = super().preco + (ProdutoFisico.peso_em_kg(self) * 5)
		return frete
		pass


class ProdutoEletronico(ProdutoFisico):

	def __init__(self, nome, preco, peso, tensao, tempo_garantia):
		super(ProdutoEletronico, self).__init__(nome, preco, peso)
		self.tensao = tensao
		self.__tempo_garantia = tempo_garantia
		pass

	
	@property
	def tensao(self):
		return self.__tensao
		pass


	@property
	def tempo_garantia(self):
		return self.__tempo_garantia
		pass

	
	@tensao.setter
	def tensao(self, nova_tensao):
		if isinstance(nova_tensao, int):
			if nova_tensao == 0 or nova_tensao == 127 or nova_tensao == 220: 
				self.__tensao = nova_tensao
			else:
				raise ValueError
		else:
			raise TypeError 
			pass

	def calcular_preco_com_frete(self):
		frete = super().calcular_preco_com_frete()
		novo_frete = frete * 1.01
		return novo_frete
		pass

class Ebook(Produto):

	def __init__(self, nome, preco, autor, numero_paginas):
		super(Ebook, self).__init__(nome, preco)
		self.__autor = autor
		self.numero_paginas = numero_paginas
		pass

	

	@property
	def nome_exibicao(self):
		return '%s (%s)' % (super().nome, self.__autor)
		pass


	@property
	def numero_paginas(self):
		return self.__numero_paginas
		pass
	

	@numero_paginas.setter
	def numero_paginas(self, valor):
		if valor > 0:
			self.__numero_paginas = valor
		else:
			raise ValueError
		pass



