num = int(input())


def simple_iteration_method(n):
    a = 0
    b = 1
    print(a, end=" ")
    print(b, end=" ")
    for i in range(n - 2):
        c = a + b
        a = b
        b = c
        print(c, end=" ")


simple_iteration_method(num)
