num=int(input())
def poss_seq(n):
    ans=1
    l=list(str(n))
    for i in range(len(l)-1):
        x=int(("").join(l[i:i+1]))
        if x<=26:
            ans+=1
        else:
            continue
    return ans

answer = poss_seq(num)
print(answer)
