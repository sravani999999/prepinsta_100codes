def is_armstrong_num(n):
    s = 0
    n1 = list(str(n))
    length = len(n1)
    for i in n1:
        s += int(i) ** length
    if n == s:
        return True
    else:
        return False


x, y = map(int, input("Enter two values (range) : ").split())
for j in range(x, y + 1):
    if is_armstrong_num(j):
        print(j)
    else:
        continue
