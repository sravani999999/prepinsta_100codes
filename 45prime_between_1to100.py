from math import sqrt
def checkPrime(n):
    if n ==1:
        return 0
    else:
        for j in range(2,int(sqrt(n))+1):
            if n%j==0:
                return 0
        return 1

a,b=1,100
for i in range(a,b+1):
    if checkPrime(i):
        print(i,end=' ')
    