num = int(input())


def convert(n):
    l = ''
    while n != 0:
        if n % 16 == 0:
            l = l + '0'
        elif 1 <= n % 16 <= 9:
            ans = str(n % 16)
            l = l + ans
        else:
            l = l + chr(55 + (n % 16))
        n //= 16
    print(l[::-1])


convert(num)
