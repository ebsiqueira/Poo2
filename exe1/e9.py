n = int(input('Primeiro int: '))
m = int(input('Segundo int: '))

a = 0

if(n<m):
    for k in range(n, m+1):
        a += k
    print('Media: %.2f' % (a/(m-n+1)))
else:
    for k in range(m, n+1):
        a += k
    print('Media: %.2f' % (a/(n-m+1)))

print('Soma: %d' % a)
