from random import randint
contagem = [0,0,0,0,0,0]
for i in range(100):
    numeroSorteado = randint(0,5)+1
    contagem[numeroSorteado-1] += 1

for i in range(6):
    print('Número de "', i+1, '" sorteados: ',contagem[i])
