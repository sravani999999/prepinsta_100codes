num = int(input())


def is_strong_num(n):
    if sum_of_fact(n) == n:
        print("It's a Strong Number")
    else:
        print("No")


def sum_of_fact(n):
    n=str(n)
    l = list(n)
    ans = 0
    for i in range(len(l)):
        ans += fact(int(l[i]))
    return ans


def fact(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans


is_strong_num(num)
