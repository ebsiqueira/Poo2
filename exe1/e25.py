for i in range(2,100000):
    for k in range(2,i+1):
        if(i%k == 0) and (i != k):
            break
        elif(i%k == 0) and (i == k):
            print(i,'é primo!')
