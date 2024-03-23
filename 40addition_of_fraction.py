numerator1, denominator1 = map(int, input().split())
numerator2, denominator2 = map(int, input().split())


def lcm(a, b):
    num1 = max(a, b)
    num2 = a + b - num1
    i = 1
    while num1 % num2 != 0:
        i += 1
        num1 *= i
    return num1


def calculate_addition(a1, b1, a2, b2):
    lcm_of_denominator = lcm(b1, b2)
    x1 = (lcm_of_denominator / b1) * a1
    x2 = (lcm_of_denominator / b2) * a2
    print((x1 + x2), "/", lcm_of_denominator)


calculate_addition(numerator1, denominator1, numerator2, denominator2)
