num = input()


def algorithmic_way(n):
    ans = 0
    j = 0
    l = list(num)
    l1 = l[::-1]
    for i in l1:
        if ord(i) >= 65 and ord(i) <= 70:
            ans += (ord(i) - 55) * (16 ** j)
            j += 1
        else:
            n = int(i)
            ans += n * (16 ** j)
            j += 1

    print(ans)


algorithmic_way(num)
