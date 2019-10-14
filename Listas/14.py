perguntas = [['Telefonou para a vítima ? '],['Esteve no local do crime ? '],['Mora perto da vítima ? '],['Devia para a vítima ? '],['Já trabalhou com a vítima ? ']]
aux = 0
for i in range(5):
    resp = input(perguntas[i][0])
    perguntas[i].append(resp)

for k in range(5):
    if(perguntas[k][1] == 'sim'):
        aux += 1

if (aux == 2):
    print('Suspeito')
elif(aux <= 4):
    print('Cúmplice')
elif(aux == 5):
    print('Assassino')
else:
    print('Inocente')