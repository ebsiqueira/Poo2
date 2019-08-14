n = int(input('Primeiro int: '))
m = int(input('Segundo int: '))

a = 0
count = 0

if(n<m):
    for k in range(n, m+1):
        if(k%2 != 0):
            a += k
            count += 1

else:
    for k in range(m, n):
        if(k%2 != 0):
            a += k
            count += 1

media =  a/count

print('Soma: %d' % a)
print('Media: %d' % media)
if(media%2 == 0):
    print('Media é Par')
else:
    print('Media é Ímpar')
