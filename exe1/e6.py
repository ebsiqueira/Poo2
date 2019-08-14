n = int(input())
m = 0

for k in range(1, n):
    if(k%3 == 0):
        m += k
print(m)
