num = int(input())


def algorithmic_way(n):
    ans = 0
    i = 0
    while n != 0:
        x = n % 10
        ans += x * (2 ** i)
        i += 1
        n //= 10

    print(ans)


def inbuilt_method(n):
    ans = int(str(n), 2)
    print(ans)


algorithmic_way(num)
inbuilt_method(num)
