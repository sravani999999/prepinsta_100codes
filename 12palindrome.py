num = input()


def simple_iterative_method(n):
    n = int(n)
    n1 = n
    ans = 0
    while n != 0:
        x = n % 10
        ans = ans * 10 + x
        n //= 10
    if n1 == ans:
        print("Woahh!! It's a Palindrome")
    else:
        print("Oops! It's not a Palindrome")


def string_slicing(n):
    s = n[::-1]
    if n == s:
        print("Woahh!! It's a Palindrome")
    else:
        print("Oops! It's not a Palindrome")


def recursion(n, ans):
    n = int(n)
    if n == 0:
        return ans
    x = n % 10
    ans = ans * 10 + x
    return recursion(int(n / 10), ans)


ans1 = str(recursion(num, 0))
print("Woahh!! It's a Palindrome") if ans1 == num else print("Oops! It's not a Palindrome")


def character_matching(str):
    for i in range(0, len(str)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True


print("Woahh!! It's a Palindrome") if character_matching(num) else print("Oops! It's not a Palindrome")

string_slicing(num)
simple_iterative_method(num)
