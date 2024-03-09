number = input()
s = 0


def string_extraction_method(n):
    s = 0
    for i in n:
        s += int(i)
    print(s)


def brute_force_method(n):
    n = int(n)
    ans = 0
    while n != 0:
        x = n % 10
        ans += x
        n //= 10
    print(ans)


def recursion_1(n, sum):
    if n == 0:
        return sum
    n = int(n)
    sum = sum + n % 10
    return recursion_1(int(n / 10), sum)


def recursion_2(n):
    n = int(n)
    if n == 0:
        return 0
    return int(n % 10) + recursion_2(int(n / 10))


def ascii_value_method(n):
    sum = 0
    for i in range(len(n)):
        sum += ord((n)[i]) - 48
    print(sum)


def inbuilt_methods(n):
    n = list(n)
    n = map(int, n)
    print(sum(n))


def one_line_recursive(n):
    n = int(n)
    return 0 if n == 0 else int(n % 10) + one_line_recursive(int(n / 10))


def cool_method(n):
    n = [int(d) for d in n]
    print(sum(n))


string_extraction_method(number)
brute_force_method(number)
print(recursion_1(number, 0))
print(recursion_2(number))
ascii_value_method(number)
inbuilt_methods(number)
print(one_line_recursive(number))
cool_method(number)
