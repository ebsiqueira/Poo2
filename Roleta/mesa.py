from roletaAmericana import Americana
from roletaEuropeia import Europeia
from roletaFrancesa import Francesa

class Mesa:
    def __init__(self, tipoRoleta):
        self.tipoRoleta = tipoRoleta
        self.listaJogadores = []
        self.listaApostas = []

    def sortearNumero(self):
        if(self.tipoRoleta == 'Americana'):
            americana = Americana()
            americana.rodar()
        elif(self.tipoRoleta == 'Europeia'):
            europeia = Europeia()
            europeia.rodar()
        elif(self.tipoRoleta == 'Francesa'):
            francesa = Francesa()
            francesa.rodar()
            
    def cadastrar(self,jogador):
        self.listaJogadores.append(jogador)

    def getJogadores(self):
        return self.listaJogadores

    def jogadoresNaMesa(self):
        for jogador in self.listaJogadores:
            print(jogador.nome)

    def fichasJogadores(self):
        for jogador in self.listaJogadores:
            print('O jogador {} possui {} fichas'.format(jogador.nome,jogador.fichas))

    def realizarAposta(self,aposta):
        self.listaApostas.append(aposta)
    
    def getApostas(self):
        return self.listaApostas

        