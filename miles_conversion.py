miles = int(input("How many miles?"))
conversion = int(input("What do you want to convert to? Enter 1 for Yards, 2 for Feet, or 3 for Inches."))
if conversion == 1:
    a = miles * 1760
    print(miles," miles = ", a, " yards.")
elif conversion == 2:
    a = miles * 5280
    print(miles," miles = ", a, " feet.")
elif conversion == 3:
    a = miles * 63360
    print(miles," miles = ", a, " yards.")
else:
    print("Sorry. That wasn't a valid input.")
