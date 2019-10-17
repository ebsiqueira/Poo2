veiculos = []
menorConsumo = 9999999999
carroMenorConsumo = ''
for i in range(5):
    print('Veículo ', i+1)
    nome = input('Nome: ')
    consumo = float(input('Km por litro: '))
    consumoTotal = 1000/consumo
    preco = consumo * 2.25
    if(consumo < menorConsumo):
        menorConsumo = consumo
        carroMenorConsumo = nome
    veiculo = [nome, consumo, consumoTotal, preco]
    veiculos.append(veiculo)

print('Relatório Final')
for i in range(5):
    print('{} - {:<20} - {:>8,.1f} - {:>8,.2f} litros - R$ {:.2f}'.format(i+1, veiculos[i][0], veiculos[i][1],veiculos[i][2],veiculos[i][3]))
print('O menor consumo é do ', carroMenorConsumo)
