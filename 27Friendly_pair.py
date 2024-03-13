import math

num1, num2 = map(int, input().split())


def more_complexity(n):
    l = []
    for i in range(1, n):
        if n % i == 0:
            l.append(i)

    return sum(l)


def less_complexity(n):
    l = []
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            if (n / i == i):
                l.append(i)
            else:
                l.append(i)
                l.append(int(n / i))
        i += 1
    return sum(l) - n


if (num1 / less_complexity(num1) == num2 / less_complexity(num2)):
    print("Friendly Pair")
else:
    print("Nope")

if (num1 / more_complexity(num1) == num2 / more_complexity(num2)):
    print("Friendly Pair")
else:
    print("Nope")
