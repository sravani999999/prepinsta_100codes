import math

num = int(input())


def prime_factors(n):
    while n % 2 == 0:
        print(2, end=" ")
        n = int(n / 2)

    for i in range(3, int(math.sqrt(n)), 2):
        while n % 3 == 0:
            print(i, end=" ")
            n = int(n / i)
    if n > 2:
        print(n, end=" ")


prime_factors(num)
