num = int(input())


def using_modulo(n):
    square_num = n * n
    last_digit = square_num % (10 ** len(str(num)))
    if num == last_digit:
        print("Automorphic Number!!")
    else:
        print("Nope!")


def using_slicing(n):
    if int(str(n ** 2)[-len(str(n))::]) == n:
        print("Automorphic Number!!")
    else:
        print("Nope!")


def using_endswith_method(n):
    square = str(n * n)
    if square.endswith(str(n)):
        print("Automorphic Number!!")
    else:
        print("Nope!")


using_modulo(num)
using_slicing(num)
using_endswith_method(num)
