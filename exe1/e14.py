n = int(input('Digite um número: '))
m = int(input('Digite um número: '))

valorFor = 1
l = 0
valorWhile = 1

# for
for k in range(m):
    valorFor *= n

# while
while(l<m):
    valorWhile *= n
    l += 1

print('For: %d' % valorFor)
print('While: %d' % valorWhile)
