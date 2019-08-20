n = input('Digite um numero N: ')

saida = ''

ate9 = ['', ' e um', ' e dois', ' e tres', ' e quatro', ' e cinco', ' e seis', ' e sete', ' e oito', ' e nove']
ate19 = ['zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezeoito', 'dezenove']
de20ate100 = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
centenaN  = ['', 'cento e ', 'duzentos e ', 'trezentos e ', 'quatrocentos e ', 'quinhentos e ', 'seiscentos e ', 'setecentos e ', 'oitocentos e ', 'novecentos e ']
centenaZerada = ['', 'cem', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']

def saidaAte99(num):
    decEuni = int(num[len(num)-2] + num[len(num)-1])
    if(decEuni < 20):
        return ate19[decEuni]
    else:
        decimal = int(n[len(n)-2])
        unidade = int(n[len(n)-1])
        return de20ate100[decimal-2] + ate9[unidade]


if(len(n) == 1):
    n = '0' + n
saida = saidaAte99(n)

if(len(n) > 2):
    centena = int(n[len(n)-3])
    decEuni = int(n[len(n)-2] + n[len(n)-1])
    if(decEuni == 0):
        saida = centenaZerada[centena]
    else:
        saida = centenaN[centena] + saida

    if(len(n) > 3):
        aux = ''
        if(len(n) == 4):
            aux = '0'+ n[len(n)-4]
        else:
            aux = n[len(n)-5] + n[len(n)-4]
        milhar = saidaAte99(aux)
        if(milhar == 'um'):
                milhar =  ''
        else:
            milhar = milhar + ' '
        if(centena == 0 or (centena != 0 and decEuni == 0)):
            saida = milhar + 'mil e ' + saida
        else:
            saida = milhar + 'mil ' + saida

print(saida)
