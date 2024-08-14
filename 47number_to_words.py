n = int(input())

def thousands(c):
    if str(c)[1]=='0':
        i = ones[(c//1000)-1]+" "+"thousand"+" "+tens(int(str(c)[2:4]))
        return i
    else:
        i = ones[(c//1000)-1]+" "+"thousand"+" "+hundreds(int(str(c)[1:4]))
        return i

def hundreds(b):
    ans = ones[(b//100)-1]+" "+"hundred"+" "+tens(int(str(b)[1:3]))
    return ans

def tens(a):
    if len(str(a))==2 and str(a)[1]=='0':
        return tens_words[(a//10)-3] 
    elif a>=1 and a<=20:
        return ones[a-1]
    else:
        x=tens_words[(a//10)-3]
        y=ones[(a%10)-1]
        return x+" "+y

ones = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty"]
tens_words = ["thirty","forty","fifty","sixty","seventy","eighty","ninty"]

if n >=1 and n<=20:
    print(ones[n-1]) 
elif len(str(n))==2 and str(n)[1]=='0':
    print(tens_words[(n//10)-3])
elif len(str(n))==2 and str(n)[1]!='0':
    p = tens(n)
    print(p)
elif n>99 and n<=999 and str(n)[1:3]=='00':
    print(ones[(n//100)-1]+" "+"hundred")
elif n>99 and n<=999 and str(n)[1:3]!='00':
    p=hundreds(n)
    print(p)
elif n>=1000 and n<=9999 and str(n)[1:4]=='000':
    print(ones[(n//1000)-1]+" "+"thousand")
elif n>=1000 and n<=9999 and str(n)[1:4]!='000' and str(n)[2:4]=='00':
    print(ones[(n//1000)-1]+" "+"thousand"+" "+ones[int(str(n)[1:4])//100-1]+ " "+"hundred")
elif n>=1000 and n<=9999 and str(n)[1:4]!='000':
    p=thousands(n)
    print(p)



