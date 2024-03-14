x, y = map(int, input().split())


def linear_quest(x, y):
    for i in range(max(x, y), (x * y) + 1):
        if i % x == i % y == 0:
            lcm = i
            break
    print(lcm)


def linear_interval_way(x, y):
    num1 = x
    num2 = y
    for i in range(max(num1, num2), 1 + (num1 * num2), max(num1, num2)):
        if i % num1 == i % num2 == 0:
            lcm = i
            break

    print(lcm)


def using_HCF(x, y):
    x = min(x, y)
    y = x + y - x
    for i in range(1, x + 1):
        if x % i == 0 and y % i == 0:
            hcf = i
    lcm = int((x * y) / hcf)
    print(lcm)


linear_quest(x, y)
using_HCF(x, y)
linear_interval_way(x, y)
