algarismos = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

romano = ''
n = input('Digite um numero: ')
for k in range(len(n)):
    i = 2*k
    casa = int(n[len(n)-1-k])
    if(casa <= 3):
        for l in range(casa):
            romano =  algarismos[i]+ romano
    elif(casa < 5):
        romano = algarismos[i+1] + romano
        for l in range(5-casa):
            romano = algarismos[i] + romano
    elif(casa <= 8):
        for l in range(casa%5):
            romano =  algarismos[i]+ romano
        romano = algarismos[i+1] + romano
    else:
        romano = algarismos[i+2] + romano
        for l in range(5-(casa%5)):
            romano =  algarismos[i]+ romano


print(romano)
