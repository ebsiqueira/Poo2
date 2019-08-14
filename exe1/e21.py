soma = 0
quantidade = 0
total = 0
maior = 0
menor = 9999999999999999

while True:

    valor = float(input('Digite o valor: '))

    if(valor == 0):
        break
    
    quantidade += 1
    soma += valor
    total += valor

    if(valor > maior):
        maior = valor

    if(valor < menor):
        menor = valor

print('Quantidade de valores lidos: ', quantidade)
print('Soma dos valores lidos: ', soma)
print('Média dos valores lidos: ', total/quantidade)
print('Maior valor lido: ', maior)
print('Menor valor lido: ', menor)