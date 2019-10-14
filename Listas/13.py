meses = [['Janeiro'],['Fevereiro'],['Março'],['Abril'],['Maio'],['Junho'],['Julho'],['Agosto'],['Setembro'],['Outubro'],['Novembro'],['Dezembro']]
media = 0
mesesA = []
for i in range(12):
    temp = float(input('Digite a temperatura no mês de {}: '.format(meses[i][0])))
    meses[i].append(temp)
    media += temp

mediaFinal = media / 12

for k in range(12):
    if(meses[k][1] > mediaFinal):
        mesesA.append(meses[i][0])

print(mesesA)
