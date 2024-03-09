num = input()


def iterative_method(n):
    power = len(n)
    n1 = int(n)
    n = int(n)
    ans = 0
    while n != 0:
        x = pow(n % 10, power)
        ans += x
        n //= 10
    if ans == n1:
        print("Armstrong")
    else:
        print("Not Armstrong")


def recursive_method(n2, ans, power):
    n2 = int(n2)
    if n2 == 0:
        return ans
    x = pow(n2 % 10, power)
    ans += x
    return recursive_method(int(n2 / 10), ans, power)


ans1 = recursive_method(num, 0, len(str(num)))
if ans1 == int(num):
    print('Armstrong')
else:
    print("Not Armstrong")

iterative_method(num)
