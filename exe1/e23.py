while True:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))

    op = int(input('(1) Adição\n(2) Subtração\n(3) Multiplicação\n(4) Divisão\n(5) Sair\nOpção: '))

    if(op == 1):
        print('{} + {} = {}'.format(n1,n2,n1+n2))
    elif(op == 2):
        print('{} - {} = {}'.format(n1,n2,n1-n2))
    elif(op == 3):
        print('{} x {} = {}'.format(n1,n2,n1*n2))
    elif(op == 4):
        print('{} / {} = {}'.format(n1,n2,n1/n2))
    elif(op == 5):
        break
    