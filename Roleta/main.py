##		if(self.tipo == 'Straight'):
##			
##		elif(self.tipo == 'Split'):
##		
##		elif(self.tipo == 'Corner'):
##
##		elif(self.tipo == 'Street'):
##
##		elif(self.tipo == 'Double Street'):
##
##		elif(self.tipo == 'Five Number'):
##
##		elif(self.tipo == 'Red'):
##
##		elif(self.tipo == 'Black'):
##
##		elif(self.tipo == 'Even'):
##
##		elif(self.tipo == 'Odd'):
##
##		elif(self.tipo == 'Dozens'):
##
##		elif(self.tipo == 'Column'):

from mesa import Mesa
from jogador import Jogador
from banca import Banca
from aposta import Aposta

while True: 
    print('1. Criar Mesa\n2. Sair')
    a = int(input('Entrada: '))
    
    if(a == 1):
        mesa = Mesa(input('Digite o tipo de roleta: '))
        banca = Banca()
        while True:
            print('1. Cadastrar Jogador\n2. Mostrar Jogadores\n3. Iniciar')
            b = int(input('Entrada: '))
        
            if(b == 1):
                jogador = Jogador(input('Digite o nome do jogador: '))
                mesa.cadastrar(jogador)
            elif(b == 2):
                mesa.jogadoresNaMesa()
            elif(b == 3):
                print('----- Fase de Apostas -----')
                listaJogadores = mesa.getJogadores()
                for jogador in listaJogadores:
                    numerosApostados= []
                    tipoAposta = input('Qual o tipo de aposta que o jogador {}({}) deseja fazer?\nEntrada: '.format(jogador.id, jogador.nome))
            		if(tipoAposta == 'Straight'):
                        n = int(input('Digite o número que deseja apostar: '))
                        numerosApostados.append(n)
            		elif(tipoAposta == 'Split'):
                        for i in range(2):
                            n = int(input('Digite o número que deseja apostar: '))
                            numerosApostados.append(n)
            		elif(tipoAposta == 'Corner'):
                        for i in range(4):
                            n = int(input('Digite o número que deseja apostar: '))
                            numerosApostados.append(n)
            		elif(tipoAposta == 'Street'):
                        n = int(input('Digite o número da fileira que deseja apostar: '))
                        numerosApostados.append((n*3)-2)
                        numerosApostados.append((n*3)-1)
                        numerosApostados.append(n*3)
            		elif(tipoAposta == 'Double Street'):
                    
            		elif(tipoAposta == 'Five Number'):
                    
            		elif(tipoAposta == 'Red'):
                    
            		elif(tipoAposta == 'Black'):
                    
            		elif(tipoAposta == 'Even'):
                    
            		elif(tipoAposta == 'Odd'):
                    
            		elif(tipoAposta == 'Dozens'):
                    
            		elif(tipoAposta == 'Column'):
                    
                    quantidadeAposta = int(input('Quantas fichas o jogador {}({}) deseja apostar?\nEntrada: '.format(jogador.id, jogador.nome)))
                    
                    while ((jogador.controleApostas == 3) and (quantidadeAposta == 0)):
                        quantidadeAposta = int(input('Quantas fichas o jogador {}({}) deseja apostar?\nEntrada: '.format(jogador.id, jogador.nome)))
                    
                    fichasApostadas = jogador.apostar(quantidadeAposta)
                    
                    print('O jogador {}({}) apostou {} fichas!'.format(jogador.id, jogador.nome, fichasApostadas))
                    
                    aposta = Aposta(tipoAposta, fichasApostadas)
                    mesa.realizarAposta(aposta)

                #listaApostas = mesa.getApostas()
                #   
                #for apostas in listaApostas:
                #   print(apostas.numFichas)

    elif(a == 2):
        break