nota = 0

for i in range(3):
    nota += float(input('Digite as notas: '))

media = nota/3

if(media < 3):
    print('Reprovado!')
elif(media <= 5.75):
    print('Exame')
else:
    print('Aprovado')
