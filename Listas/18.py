votos = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
camisa = 0
k = 0
maior = 0
segundoMaior = 0
terceiroMaior = 0
camisaMaior = 0
camisaSegundoMaior = 0
camisaTerceiroMaior = 0

while True:
    n = int(input('Digite o numero do melhor jogador: '))
    
    if (n == 0):
        break
    
    votos[n-1] += 1
    k += 1

maior = max(votos)
x = votos.index(maior)
votos[x] = 0

segundoMaior = max(votos)
y = votos.index(max(votos))
votos[y] = 0

terceiroMaior = max(votos)
z = votos.index(max(votos))
votos[z] = 0

print('Foram computados {} votos.'.format(k))
print('Jogadores          Votos         %')
print('        {}              {}         {:.1f}'.format(x+1, maior, (maior/k)*100))
print('        {}              {}         {:.1f}'.format(y+1, segundoMaior, (segundoMaior/k)*100))
print('        {}              {}         {:.1f}'.format(z+1, terceiroMaior, (terceiroMaior/k)*100))
print('O melhor jogador foi o número {}, com {} votos, correspondendo a {:.1f} porcento do total de votos.'.format(x+1, maior, (maior/k)*100))