cont = 20

a = int(input('Digite o comprimento inicial da barra A: '))
b = int(input('Digite o comprimento inicial da barra B: '))

while(a>b):
    a += 2
    b += 3.5

    cont += 1

print(cont+1)