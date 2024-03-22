number_of_people = int(input("Enter number of people: "))
number_of_seats = int(input("Enter number of seats: "))


def factorial(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans


denominator = number_of_people - number_of_seats
print(denominator)
possible_arrangements = factorial(number_of_people) / factorial(denominator)

print("Total possible arrangements:", int(possible_arrangements))
