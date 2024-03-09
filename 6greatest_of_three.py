n1, n2, n3 = map(int, input().split())


def if_else_stmts(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(num1, " is greatest")
    elif (num2 > num3):
        print(num2, " is greatest")
    else:
        print(num3, " is greatest")


def nested_if_else_stmts(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            print(num1)
        else:
            print(num3)
    else:
        if num2 > num3:
            print(num2)
        else:
            print(num3)


def inbuilt_function(num1, num2, num3):
    print(max(num1, num2, num3))


def ternary_operator(num1, num2, num3):
    max = num1 if num1 > num2 else num2
    max = max if max > num3 else num3
    print(max)


if_else_stmts(n1, n2, n3)
nested_if_else_stmts(n1, n2, n3)
ternary_operator(n1, n2, n3)
inbuilt_function(n1, n2, n3)
