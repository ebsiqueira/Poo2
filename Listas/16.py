from math import floor

vendasPVendedor = [3000, 6000, 4500, 4200, 4300, 5900, 900000]

salarios = []
for vendedor in vendasPVendedor:
    salario = 200 + vendedor*0.09
    salarios.append(salario)

contagemNosIntervalos = [0,0,0,0,0,0,0,0,0]
for salario in salarios:
    indice = floor((salario-200)/100)
    if(indice > 8):
        indice = 8
    contagemNosIntervalos[indice] += 1
print('Salarios:\n', salarios)
print('Salarios entre $200-$299: ', contagemNosIntervalos[0])
print('Salarios entre $300-$399: ', contagemNosIntervalos[1])
print('Salarios entre $400-$499: ', contagemNosIntervalos[2])
print('Salarios entre $500-$599: ', contagemNosIntervalos[3])
print('Salarios entre $600-$699: ', contagemNosIntervalos[4])
print('Salarios entre $700-$799: ', contagemNosIntervalos[5])
print('Salarios entre $800-$899: ', contagemNosIntervalos[6])
print('Salarios entre $900-$999: ', contagemNosIntervalos[7])
print('Salarios entre $1000 em diante: ', contagemNosIntervalos[8])
