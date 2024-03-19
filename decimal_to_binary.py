num = int(input())


def convert(n):
    l = ''
    while n != 0:
        if n % 2 == 0:
            l = l + '0'
        else:
            l = l + '1'
        n //= 2
    ans = "".join(l)
    print(ans)


convert(num)
