import math

num = int(input())


def using_more_time_complexity(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=" ")


def using_less_time_complexity(n):
    l=[]
    for i in range(1, int(math.sqrt(n))):
        if n % i == 0:
            l.append(i)
            l.append(int(n/i))
    l.sort()
    print(l)

using_more_time_complexity(num)
print("\n")
using_less_time_complexity(num)
