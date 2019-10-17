numeros = []
soma = 0
media = 0
aMedia = 0
mSete = 0

while True:
    n = int(input('Digite um valor: '))

    if(n == -1):
        print('Obrigado por usar o programa')
        break

    numeros.append(n)

    print(len(numeros))
    
    print(numeros)
    
    soma = 0
    numeros.reverse()
    for num in numeros:
        print(num)
        soma += num
    print(soma)

    media = soma/len(numeros)
    print(media)

    aMedia = 0
    for i in numeros:
        if (i > media):
            aMedia += 1
        if (i < 7):
            mSete += 1
    print(aMedia)
    print(mSete)
    

    

    