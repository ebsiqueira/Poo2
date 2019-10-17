while True:
    atleta = []

    nome = input('Digite o nome do atleta: ')
    if(nome == ''):
        break
    atleta.append(nome)

    for i in range(5):
        nota = float(input('Digite a distância do pulo: '))
        atleta.append(nota)

    media = 0
    for k in range(1,6):
        media += atleta[k]
    mediaFinal = media/5

    print(atleta[0],'\n')
    print('Primeiro Salto: {} m'.format(atleta[1]))
    print('Segundo Salto: {} m'.format(atleta[2]))
    print('Terceiro Salto: {} m'.format(atleta[3]))
    print('Quarto Salto: {} m'.format(atleta[4]))
    print('Quinto Salto: {} m'.format(atleta[5]))
    print('\nResultado Final: ')
    print('Atleta:',atleta[0])
    print('Saltos: {} - {} - {} - {} - {}'.format(atleta[1],atleta[2],atleta[3],atleta[4],atleta[5]))
    print('Média dos saltos: {} m'.format(mediaFinal))

    
