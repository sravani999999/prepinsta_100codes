number = int(input("Enter a number \n"))


def brute_force(num):
    if num % 2 == 0:
        print('even')
    else:
        print('odd')


def ternary_operator(num):
    print('even' if num % 2 == 0 else 'odd')


def bitwise(num):
    if num & 1 == 0:
        print('even')
    else:
        print('odd')


brute_force(number)
bitwise(number)
ternary_operator(number)
