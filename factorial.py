num = int(input())


def find_factorial(n):
    ans = 1
    for i in range(n, 1, -1):
        ans *= i
    print(ans)


find_factorial(num)
