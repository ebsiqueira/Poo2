cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0


saque = int(input('Digite o valor a ser sacado: '))

while True:
    if(saque >= 100):
        cem += 1
        saque -= 100
    elif(saque >= 50):
        cinquenta += 1
        saque -= 50
    elif(saque >= 20):
        vinte += 1
        saque -= 20
    elif(saque >= 10):
        dez += 1
        saque -= 10
    elif(saque >= 5):
        cinco += 1
        saque -= 5
    elif(saque >= 2):
        dois += 1
        saque -= 2
    elif(saque >= 1):
        um += 1
        saque -= 1
    elif(saque < 1):
        break

print('Notas de cem: {}\nNotas de cinquenta: {}\nNotas de vinte: {}\nNotas de dez: {}\nNotas de cinco: {}\nNotas de dois: {}\nMoedas de um: {}'.format(cem,cinquenta,vinte,dez,cinco,dois,um))