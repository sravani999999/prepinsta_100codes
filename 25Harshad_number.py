num = int(input())


def simple_method(n):
    total_sum = list(str(n))
    total_sum_1 = [int(i) for i in total_sum]
    total_sum_2 = sum(total_sum_1)
    if n % total_sum_2 == 0:
        print("Harshad Number!!")
    else:
        print("Nope!")


def using_iteration(n):
    n1 = n
    ans = 0
    while n != 0:
        x = n % 10
        ans += x
        n = n // 10
    if n1 % ans == 0:
        print("Harshad Number!!")
    else:
        print("Nope!")


simple_method(num)
using_iteration(num)
