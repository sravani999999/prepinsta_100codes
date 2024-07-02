num=int(input())
def method_1(n):
    ans=0
    while n!=0:
        n//=10
        ans+=1
    print(ans)

def method_2(n):
    n=list(str(n))
    print(len(n))

method_1(num)
method_2(num)