votos = []
windows = 0
unix = 0
linux = 0
net = 0
mac = 0
outro = 0

while True:
    print('Qual o melhor sistema operacional para uso em servidores ?\n')
    print('1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro')
    n = int(input('Resposta: '))

    if (n == 0):
        break

    if (n > 0 and n <= 6):
        votos.append(n)

    else:    
        print('Digite um valor válido!')


for numero in votos:
    if(numero == 1):
        windows += 1
    elif(numero == 2):
        unix += 1
    elif(numero == 3):
        linux += 1
    elif(numero == 4):
        net += 1
    elif(numero == 5):
        mac += 1
    elif(numero == 6):
        outro += 1

total = windows + unix + mac + linux + net + outro

mediaWindows = (windows/len(votos)) * 100
mediaUnix = (unix/len(votos)) * 100
mediaLinux = (linux/len(votos)) * 100
mediaNet = (net/len(votos)) * 100
mediaMac = (mac/len(votos)) * 100
mediaOutro = (outro/len(votos)) * 100

print('Sistema Operacional    Votos   %')
print('-------------------    -----  ---')
print('Windows Server             {}  {:.1f}%'.format(windows,mediaWindows))
print('Unix                       {}  {:.1f}%'.format(unix,mediaUnix))
print('Linux                      {}  {:.1f}%'.format(linux,mediaLinux))
print('Netware                    {}  {:.1f}%'.format(net,mediaNet))
print('Mac OS                     {}  {:.1f}%'.format(mac,mediaMac))
print('Outro                      {}  {:.1f}%'.format(outro,mediaOutro))
print('-------------------    -----')
print('Total                     {}'.format(total))

    
    


