n = int(input('Insira um numero maximo: '))
m = 0

for k in range(1,n):
    if(k%3 == 0) or (k%5 == 0) or (k%7 == 0):
        m += k
    if(k%8 == 0):
        m -= k

print(m)
