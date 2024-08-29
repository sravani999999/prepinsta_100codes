def using_recursion(n, i=2):
    if n==i:
        return True
    elif n%i==0:
        return False
    else:
        return using_recursion(n,i+1)
    

def using_loop(n):
    for i in range(2,n):
        if n%i==0:
            print("Not Prime")
            break
        else:
            print("Prime")
    
num = int(input())
ans = using_recursion(num,2)
print("Prime" if ans else "Not Prime")
using_loop(num)