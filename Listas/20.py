print('Projeção de gastos com abono:')
print('=============================')
salarios = []
salario = -1
while(salario != 0):
    salario = int(input('Salario:'))
    salarios.append(salario)

salarios.remove(0)

abonoTotal = 0
contValorMinimo = 0
maiorAbono = 0

print('\nSalario      -   Abono')
for salario in salarios:
    abono = salario*0.2

    if(abono <= 100):
        abono = 100
        contValorMinimo += 1

    if(abono > maiorAbono):
        maiorAbono = abono

    abonoTotal+= abono
    v

print('Foram processados ', len(salarios), ' colaboradores')
print('Total gasto com abonos: R${:.2f}'.format(abonoTotal))
print('Valor minímo pago a ',contValorMinimo, ' colaboradores')
print('Maior valor de abono pago: R${:.2f}'.format(maiorAbono))
