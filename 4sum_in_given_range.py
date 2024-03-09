n1, n2 = map(int, input().split())


def brute_force(num1, num2):
    total = 0
    for i in range(num1, num2 + 1):
        total += i
    print(total)


def formula(num1, num2):
    total2 = (num2 * (num2 + 1)) / 2
    total1 = (num1 * (num1 + 1)) / 2
    print(total2 - total1 + num1)


def recursion(num1, num2):
    if num2 == num1:
        return num1
    return num2 + recursion(num1, num2 - 1)


brute_force(n1, n2)
formula(n1, n2)
print(recursion(n1, n2))
