base = int(input())
power = int(input())


def recursion(b, p):
    if p < 2:
        return b
    return recursion(b*base, p-1)

def direct_method(b, p):
    print(b**p)

def loop(b, p):
    ans = 1
    for i in range(p):
        ans *= b
    print(ans)


ans = recursion(base, power)
print(ans)
direct_method(base, power)
loop(base, power)