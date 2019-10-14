aux = 0
for alunos in range(10):
    notas = 0
    print('------------------------')
    
    for valores in range(4):
        nota = float(input('Digite a nota: '))
        notas += nota
    
    media = notas / 4
    
    if (media >= 7):
        aux += 1

print(aux)