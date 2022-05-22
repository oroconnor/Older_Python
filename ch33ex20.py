integers = []
reals = []
count = 0
while count < 12:
    x = input("Please enter a number:")
    try:
        x = int(x)
        integers.append(x)
    except ValueError:
        try:
            x = float(x)
            reals.append(x)
        except ValueError:
            print("This is not a number.")
    count += 1
    
print("Integers:", integers)
print("Reals:", reals)
