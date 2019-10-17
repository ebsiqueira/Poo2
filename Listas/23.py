def bytesToMB(bytes):
    return bytes/10**6

print('Insira o nome de usuario seguido pelo espaço ocupado no servidor (0 para terminar):')

users = []

while True:
    u = input().split()

    if u[0] == '0':
        break

    users.append((u[0], bytesToMB(int(u[1]))))

print('ACME Inc.{:>14}Uso do espaço em disco dos usuários'.format(''))
print('{:->58}'.format(''))
print('Nr.{:>4}Usuário{:>8}Espaço Utilizado{:>8}Uso do disco'.format('', '', ''))
print('')

total = 0
for user in users:
    total += user[1]
media = total/len(users)

for k in range(len(users)):
    n = k+1
    user = users[k][0]
    espaco = users[k][1]
    pct = (espaco/total)*100
    print('{:>2} {:>11} {:>21.2f}MB {:>18.2f}%'.format(n, user, espaco, pct))

print('\nEspaço total ocupado: %.2fMB' % total)
print('Espaço medio ocupado: %.2fMB' % media)
