num = int(input())


def octal_to_decimal(n):
    ans = 0
    i = 0
    while n != 0:
        x = n % 10
        ans += x * (8 ** i)
        i += 1
        n //= 10
    decimal_to_binary(ans)


def decimal_to_binary(n):
    l = ''
    while n != 0:
        if n % 2 == 0:
            l = l + '0'
        else:
            l = l + '1'
        n //= 2
    ans = "".join(l)
    print(ans[::-1])


octal_to_decimal(num)
