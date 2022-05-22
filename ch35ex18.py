def amount_to_pay(minutes):
    if minutes <= 600:
        rate = 0
    elif minutes <= 1200:
        rate = .01
    else:
        rate = .02
    charge = (10 + minutes * rate) * 1.11
    return charge

#main code
minutes = int(input("Please enter the minutes you used last month:"))
print("Your amount to pay is: $",amount_to_pay(minutes))
