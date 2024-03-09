number = int(input("Enter a number\n"))


def brute_force(num):
    total = 0
    for i in range(num + 1):
        total += i
    print(total)


def formula(num):
    total = (num * (num + 1)) / 2
    print(total)


def recursion(num):
    if num == 1:
        return 1
    return num + recursion(num - 1)


brute_force(number)
formula(number)
print(recursion(number))
