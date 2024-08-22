num = int(input())
divisors = int(input())

def my_naive_approach(n,d):
    count = 0
    if d == 1 or n == 1:
        print(1)
    else:
        for i in range(2,n+1):
            c=0
            for j in range(1,i+1):
                if(i%j==0):
                    c+=1
            if c == d:
                count+=1
    print(count)


my_naive_approach(num, divisors)

                    

        



