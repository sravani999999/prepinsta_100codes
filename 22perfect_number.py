num = int(input())


def is_perfect_number(n):
    l = []
    for i in range(1, n):
        if n % i == 0:
            l.append(i)
    if sum(l) == n:
        print("It's a Perfect Number!")
    else:
        print("No")


is_perfect_number(num)
