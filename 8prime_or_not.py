number = int(input())


def simple_iterative_solution(n):
    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1
    if c == 2:
        print("prime")
    else:
        print("nop")


def optimization_by_break_condition(n):
    c = 0
    for i in range(2, n):
        if n % i == 0:
            c = 1
            break
    if c == 1:
        print("nop")
    else:
        print("prime")


def optimization_by_half_iterations(n):
    c = 0
    for i in range(2, int(n / 2 + 1)):
        if n % i == 0:
            c = 1
            break
    if c == 1:
        print("nop")
    else:
        print("prime")


def optimization_by_root_iterations(n):
    c = 0
    for i in range(2, int(pow(n, 0.5) + 1)):
        if n % i == 0:
            c = 1
            break
    if c == 1:
        print("nop")
    else:
        print("prime")


def optimization_by_skipping_even_ieration(num):
    flag=0
    if num < 2:
        flag = 1
    elif num == 2:
        flag = 0
    else:
        for i in range(3, int(pow(num, 0.5) + 1), 2):
            if num % i == 0:
                flag = 1
                break

    if flag == 1:
        print('nop')
    else:
        print("Prime")


def recursion(num, iter=2):
    if num == iter:
        return True
    if num % iter == 0:
        return False
    if num < 2:
        return False
    return recursion(num, iter + 1)


if recursion(number, 2):
    print("Prime")
else:
    print("Nop")

simple_iterative_solution(number)
optimization_by_half_iterations(number)
optimization_by_root_iterations(number)
optimization_by_skipping_even_ieration(number)
optimization_by_break_condition(number)
