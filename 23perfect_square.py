num = int(input())
import math


def method_1(n):
    ans = int(math.sqrt(n))
    if ans*ans == n:
        print("Purrfect Sqware!!!")
    else:
        print("Nope!")

def method_2(n):
    if(math.ceil(math.sqrt(n)) == math.floor(math.sqrt(n))):
        print("Purrfect Sqware!!!")
    else:
        print("Nope!")

method_1(num)
method_2(num)
