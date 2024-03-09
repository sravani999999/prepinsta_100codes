a, b = map(int, input().split())


def optimization_1(a, b):
    primes = []
    for i in range(a, b + 1):
        flag = 0
        if i < 2:
            continue
        elif i == 2:
            primes.append(2)
            continue
        for j in range(2, i):
            if i % j == 0:
                flag = 1
                break

        if flag == 0:
            primes.append(i)
    print(primes)


def optimization_2(a, b):
    primes = []
    for i in range(a, b + 1):
        flag=0
        if b < 2:
            continue
        elif b == 2:
            primes.append(2)
        elif b > 2:
            for j in range(2, int(i / 2) + 1):
                if i % j == 0:
                    flag=1
                    break


        if flag == 0:
            primes.append(i)
    print(primes)


def optimization_3(a, b):
    primes = []
    for i in range(a, b + 1):
        flag=0
        if b < 2:
            continue
        elif b == 2:
            primes.append(2)
        elif b > 2:
            for j in range(2, int(pow(i, 0.5) + 1)):
                if i % j == 0:
                    flag=1
                    break
        if flag == 0:
            primes.append(i)
    print(primes)


def optimization_4(a, b):
    primes = []
    for i in range(a, b + 1):
        flag = 0
        if i < 2:
            continue
        elif i % 2 == 0:
            continue
        elif i == 3:
            primes.append(3)
        elif i > 3:
            for j in range(3, int(pow(i, 0.5) + 1), 2):
                if i % j == 0:
                    flag = 1
                    break

        if flag == 0:
            primes.append(i)
    print(primes)



optimization_1(a, b)
optimization_2(a, b)
optimization_3(a, b)
optimization_4(a, b)
