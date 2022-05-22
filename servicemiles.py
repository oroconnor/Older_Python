miles = int(input("What is your car's current mileage?"))
a = miles % 12000
if a <= 6000:
    b = 6000 - a
    print("Your next service is in ", b," miles.")
    print("It is a minor service.")
else:
    b = 12000 - a
    print("Your next service is in ", b," miles.")
    print("It is a major service.")

