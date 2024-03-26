num = int(input())


def easy_way(n):
    l = list(str(num))
    for i in range(len(l)):
        if l[i] == '0':
            l[i] = '1'

    ans = "".join(l)
    print(ans)


def another_way(n):
    n1 = n
    i = 1
    while n != 0:
        x = n % 10
        if x == 0:
            n1 = n1 + 1 * i
        i = i * 10
        n //= 10

    print(n1)


easy_way(num)
another_way(num)
