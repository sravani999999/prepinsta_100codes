numerator1, denominator1 = map(int, input("Enter numerator and denominator of first fraction").split())
numerator2, denominator2 = map(int, input("Enter numerator and denominator of second fraction").split())


def lcm(a, b):
    num1 = max(a, b)
    num2 = a + b - num1
    temp = num1
    i = 1
    while num1 % num2 != 0:
        i += 1
        num1 = temp * i
    return num1


def calculate_addition(a1, b1, a2, b2):
    lcm_of_denominator = lcm(b1, b2)
    x1 = (lcm_of_denominator / b1) * a1
    x2 = (lcm_of_denominator / b2) * a2
    numerator = (x1 + x2)
    denominator = lcm_of_denominator
    simplify(numerator, denominator)


def simplify(a, b):
    new_lcm = lcm(a, b)
    hcf = int((a * b) / new_lcm)
    while b % hcf == 0 and a % hcf == 0:
        a = int(a / hcf)
        b = int(b / hcf)

    print("The final result after simplification is", a, "/", b)


calculate_addition(numerator1, denominator1, numerator2, denominator2)
