x, y = map(int, input().split())


def linear_quest(x, y):
    x = min(x, y)
    y = x + y - x
    for i in range(1, x + 1):
        if x % i == 0 and y % i == 0:
            hcf = i
    print(hcf)


def euclidean_method(x, y):
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    print(x)


linear_quest(x, y)
euclidean_method(x, y)
