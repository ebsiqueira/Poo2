votos = []
esfera = 0
limpeza = 0
cabo = 0
quebrado = 0

while True:
    print('Qual a situação do mouse ?\n')
    print('1- Necessita de esfera\n2- Necessita de limpeza\n3- Necessita troca do cabo ou conector\n4- Quebrado ou inutilizado')
    n = int(input('Resposta: '))

    if (n == 0):
        break

    if (n > 0 and n <= 4):
        votos.append(n)

    else:    
        print('Digite um valor válido!')


for numero in votos:
    if(numero == 1):
        esfera += 1
    elif(numero == 2):
        limpeza += 1
    elif(numero == 3):
        cabo += 1
    elif(numero == 4):
        quebrado += 1

total = esfera + limpeza + cabo + quebrado

mediaEsfera = (esfera/len(votos)) * 100
mediaLimpeza = (limpeza/len(votos)) * 100
mediaCabo = (cabo/len(votos)) * 100
mediaQuebrado = (quebrado/len(votos)) * 100

print('\nQuantidade de mouses = ', total,'\n')
print('Situação                     Quantidade          Percentual')
print('Necessita de esfera                   {}               {:.1f}%'.format(esfera,mediaEsfera))
print('Necessita de limpeza                  {}               {:.1f}%'.format(limpeza,mediaLimpeza))
print('Necessita troca de cabo ou conector   {}               {:.1f}%'.format(cabo,mediaCabo))
print('Quebrado ou inutilizado               {}               {:.1f}%'.format(quebrado,mediaQuebrado))

    
    


