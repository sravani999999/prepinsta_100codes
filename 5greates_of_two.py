n1, n2 = map(int, input().split())


def if_else_stmts(num1, num2):
    if num1 > num2:
        print(num1, " is greater")
    elif (num2 > num1):
        print(num2, " is greater")
    else:
        print("equal")


def ternary_operator(num1, num2):
    print(num1 if num1 > num2 else num2)


def inbuilt_function(num1, num2):
    print(max(num1, num2))


if_else_stmts(n1, n2)

ternary_operator(n1, n2)
inbuilt_function(n1, n2)
