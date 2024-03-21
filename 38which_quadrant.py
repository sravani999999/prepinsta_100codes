print("Enter the X and Y values to find out which quadrant they belong to: ", end="")
x, y = map(int, input().split())

if x > 0 and y > 0:
    print(f"The co-ordinate {x, y} lies in first quadrant ")
elif x > 0 > y:
    print(f"The co-ordinate {x, y} lies in second quadrant ")
elif x < 0 < y:
    print(f"The co-ordinate {x, y} lies in third quadrant ")
elif x < 0 and y < 0:
    print(f"The co-ordinate {x, y} lies in fourth quadrant ")
elif x != 0 and y == 0:
    print(f"The co-ordinate {x, y} lies on X-axis ")
elif x == 0 and y != 0:
    print(f"The co-ordinate {x, y} lies on Y-axis ")
elif x == 0 and y == 0:
    print(f"The co-ordinate {x, y} on origin")
