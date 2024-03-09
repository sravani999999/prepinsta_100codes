number = int(input("Enter a number\n"))


def brute_force(num):
    if num > 0:
        print('positive')
    elif num < 0:
        print('negative')
    else:
        print('zero')


def if_else_stmts(num):
    if num >= 0:
        if num == 0:
            print('zero')
        else:
            print('positive')
    else:
        print('negative')


def ternary_operator(num):
    print('positive' if num >= 0 else 'negative')


brute_force(number)
if_else_stmts(number)
ternary_operator(number)
