days = ['Quarta','Quinta', 'Sexta', 'Sabado', 'Domingo', 'Segunda', 'Terca']
months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
'Novembro', 'Dezembro']

n = int(input('Digite o número do dia: '))

d = days[n%7]


if(n<=31 and n>0):
    i = n
    m = months[0]
elif(n>31 and n<=59):
    i = n - 31
    m = months[1]
elif(n>59 and n<=90):
    i = n - 59
    m = months[2]
elif(n>90 and n<=120):
    i = n - 90
    m = months[3]
elif(n>120 and n<=151):
    i = n - 120
    m = months[4]
elif(n>151 and n<=81):
    i = n - 151
    m = months[5]
elif(n>181 and n<=212):
    i = n - 181
    m = months[6]
elif(n>212 and n<=243):
    i = n - 212
    m = months[7]
elif(n>243 and n<=273):
    i = n - 243
    m = months[8]
elif(n>273 and n<=304):
    i = n - 273
    m = months[9]
elif(n>304 and n<=334):
    i = n - 304
    m = months[10]
elif(n>334 and n<=365):
    i = n - 334
    m = months[11]

print('{}, {} de {}'.format(d,i,m))
