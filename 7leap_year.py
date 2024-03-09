import calendar

year = int(input())


def if_else_stmts1(n):
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        print("leap year")
    else:
        print("nop")


def if_else_stmts2(n):
    if ((n % 4 == 0) and (n % 100 != 0)) or (n % 400 == 0):
        print("leap year")
    else:
        print("nop")


def ternaty_op(n):
    print("leap year" if ((n % 4 == 0) and (n % 100 != 0)) or (n % 400 == 0) else "nop")


def calendar_module(n):
    if calendar.isleap(n):
        print("leap year")
    else:
        print("nop")


def lambda_function(n):
    is_leap_year = lambda n: (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0)
    if is_leap_year(n):
        print(n, " is a leap year")
    else:
        print(n, "is not a leap year.")


if_else_stmts1(year)
if_else_stmts2(year)
ternaty_op(year)
lambda_function(year)
calendar_module(year)
