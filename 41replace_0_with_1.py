num = int(input())


def easy_way(n):
    l = list(str(num))
    for i in range(len(l)):
        if l[i] == '0':
            l[i] = '1'

    ans = "".join(l)
    print(ans)


easy_way(num)
