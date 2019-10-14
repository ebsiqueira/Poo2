user_1 = []
user_2 = []
user_3 = []
user_4 = []
user_5 = []

for i in range(1,6):
    if(i == 1):
        user_1 = [int(input('Digite a idade: ')), float(input('Digite a altura: '))]
    elif(i == 2):
        user_2 = [int(input('Digite a idade: ')), float(input('Digite a altura: '))]
    elif(i == 3):
        user_3 = [int(input('Digite a idade: ')), float(input('Digite a altura: '))]
    elif(i == 4):
        user_4 = [int(input('Digite a idade: ')), float(input('Digite a altura: '))]
    elif(i == 5):
        user_5 = [int(input('Digite a idade: ')), float(input('Digite a altura: '))]

user_1.reverse()
user_2.reverse()
user_3.reverse()
user_4.reverse()
user_5.reverse()

print(user_1)
print(user_2)
print(user_3)
print(user_4)
print(user_5)
