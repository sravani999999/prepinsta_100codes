import math

num = int(input())


def more_complexity(n):
    l = []
    for i in range(1, n):
        if n % i == 0:
            l.append(i)
    if sum(l) > n:
        print("Abundant Number!!")
    else:
        print("Nope!")


def less_complexity(n):
    l = []
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            l.append(i)
            l.append(int(n / i))
    l.append(1)

    if sum(l) > n:
        print("Abundant Number!!")
    else:
        print("Nope!")


more_complexity(num)
less_complexity(num)
