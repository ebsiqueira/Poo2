vetor = ['a','b','c','d','e','f','g','h','i','j']

for letras in vetor:
    if(letras == 'a' or letras == 'e' or letras == 'i' or letras == 'o' or letras == 'u'):
        vetor.remove(letras)

print(vetor)