num = int(input())


def range_of_primes(n):
    a = []
    for i in range(2, n + 1):
        c = 0
        for j in range(1, i + 1):
            if i % j == 0:
                c += 1
        if c == 2:
            a.append(i)
    return a


def sum_of_primes(n):
    r = range_of_primes(n)
    for i in range(len(r)):
        for j in range(i):
            if r[i] + r[j] == n:
                print("Sum of prime for", n, "is:", r[i], "+", r[j], "=", n)


sum_of_primes(num)

range_of_primes(num)
