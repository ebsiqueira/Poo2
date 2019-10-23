arq = open('intraday_5min_MSFT.csv', 'r')
texto = arq.readlines()
for linha in texto :
    coluna = linha.split(',')
    for i in range(len(coluna)):
        if(i == 5):
            coluna[i] = coluna[i][0:(len(coluna[i]) - 1)]
    print(coluna)
arq.close()