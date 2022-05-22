x = 0
while True:
    x = int(input("Please enter your monthly electric usage in kWh:"))
    if x == -1: break
    while x < -1:
        x = int(input("Sorry, please enter a non-negative number:"))
    else:
        if x <= 400:
            y = .11
        elif x <= 1500:
            y = .22
        elif x <= 3500:
            y = .25
        else:
            y = .5
        z = x * y * 1.25
    print("Your total amount to pay is:",z)
print("The End")
