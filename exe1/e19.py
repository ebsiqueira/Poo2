total = 0
cont = 0

while True:
    val = float(input('Digite os valores de energia: '))

    if(val == 0):
        break

    total += val
    cont += 1
print(total / cont)