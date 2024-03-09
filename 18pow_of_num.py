import math


def using_pow_function(a, b):
    ans = pow(a, b)
    print(ans)


def using_simple_iteration(a, b):
    ans = 1
    for i in range(b):
        ans *= a
    print(ans)


def using_python_operator(a, b):
    ans = a ** b
    print(ans)


x, y = map(int, input().split())

using_pow_function(x, y)
using_simple_iteration(x, y)
using_python_operator(x, y)
