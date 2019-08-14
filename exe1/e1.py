def isPar(n):
	return n%2 == 0

n = int(input())
if(n!=0):
	if(isPar(n)):
		print('Par!')
	else:
		print('Ímpar!')
else:
	print('Zero')