class Jogador:
	totalDeJogadores = 0
	def __init__(self, nome):
		self.id = Jogador.totalDeJogadores
		Jogador.totalDeJogadores += 1
		self.nome = nome
		self.fichas = 100
		self.controleApostas = 0

	def receber(fichas):
		self.fichas += fichas

	def apostar(self, fichas):
		if (fichas == 0):
			self.controleApostas += 1
			return 0
		elif (fichas > self.fichas):
			fichas = self.fichas
			self.fichas = 0
			return fichas
		else: 
			self.fichas -= fichas
			return fichas