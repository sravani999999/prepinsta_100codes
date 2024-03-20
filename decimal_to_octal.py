num = int(input())


def convert(n):
    l = ''
    while n != 0:
        if n % 8 == 0:
            l = l + '0'
        else:
            ans = str(n % 8)
            l = l + ans
        n //= 8
    print(l[::-1])


convert(num)
