n = int(input('Digite um inteiro maior que 1: '))

for k in range(2,n+1):
    if(n%k == 0) and (n != k):
        print('Não é primo!')
        break
    elif(n%k == 0) and (n == k):
        print('É primo!')
