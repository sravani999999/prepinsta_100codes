num = int(input())


def simple_iteration_method(n):
    a = 0
    b = 1
    for i in range(n - 2):
        c = a + b
        a = b
        b = c
    print(c)


simple_iteration_method(num)
