vetor = []
par = []
impar = []

for i in range(20):
    num = int(input('Digite um numero: '))
    vetor.append(num)

    if(num%2 == 0):
        par.append(num)
    else:
        impar.append(num)

print(vetor)
print(par)
print(impar)