notas = []
valor = 0
for i in range(4):
    nota = float(input('Digite a nota do aluno: '))
    notas.append(nota)

for val in notas:
    valor += val

print(notas)
print(valor/4)