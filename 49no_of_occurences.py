def using_loops(num,a):
    c=0
    while num!=0:
        x = num%10
        if x==a:
            c+=1
        num//=10
    print(c)

def using_strings(num,a):
    str1=str(num)
    str2=str(a)
    c = str1.count(str2)
    print(c)

n = int(input())
o = int(input())

using_loops(n,o)
using_strings(n,o)
