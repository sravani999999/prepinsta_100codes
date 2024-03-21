num = int(input())


def binary_to_decimal(n):
    ans = 0
    i = 0
    while n != 0:
        x = n % 10
        ans += x * (2 ** i)
        i += 1
        n //= 10
    decimal_to_octal(ans)


def decimal_to_octal(n):
    l = ''
    while n != 0:
        if n % 8 == 0:
            l = l + '0'
        else:
            ans = str(n % 8)
            l = l + ans
        n //= 8
    print(l[::-1])

binary_to_decimal(num)
