print("Please enter the three lengths of the sides of your triangle.")
a = int(input("First side length:"))
b = int(input("Second side length:"))
c = int(input("Third side length:"))
if a >= b + c:
    print("Sorry, those are not valid lengths for a triangle.")
elif b >= a + c:
     print("Sorry, those are not valid lengths for a triangle.")
elif c >= a + b:
     print("Sorry, those are not valid lengths for a triangle.")
else:
    if a == b == c:
        print("This triangle is equilateral.")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("This triangle is right angled.")
    else:
        print("This triangle is not special.")
