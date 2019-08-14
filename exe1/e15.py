fib = []

def fibonacci(n):
    if n <= 1:
        return n

    if fib[n] != 0:
        return fib[n]
    else:
        fib[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return fib[n]

n = int(input('Digite um número: '))

for k in range(n):
    fib.append(0)
    print(fibonacci(k))
