month = int(input("What month is it? Enter a number 1-12."))
if month == 12 or month <=2:
    print("It is Winter.")
elif month >= 3 and month <= 5:
    print("It is Spring.")
elif month >= 6 and month <= 8:
    print("It is Summer.")
else:
    print("It is Fall.")
    
