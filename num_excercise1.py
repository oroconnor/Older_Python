x = int(input("Please enter a number:"))
if x > 0:
    if x % 10 == 0:
        print("Last digit equal to 0")
    else:
        if x % 10 == 1:
            print("Last digit equal to 1")
        else:
            print("None")
else:
    if x == -1:
        print("Bye")
    else:
        print("Invalid Number")
