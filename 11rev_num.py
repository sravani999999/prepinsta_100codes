num = input()


def simple_iterative_method(n):
    n = int(n)
    ans = 0
    while n != 0:
        x = n % 10
        ans = ans * 10 + x
        n //= 10
    print(ans)


def string_slicing(n):
    print(n[::-1])


def recursion(n, ans):
    n = int(n)
    if n == 0:
        return ans
    x = n % 10
    ans = ans * 10 + x
    return recursion(int(n / 10), ans)


simple_iterative_method(num)
string_slicing(num)
print(recursion(num, 0))
