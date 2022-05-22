def display_menu():
    print("Please choose from the following options:")
    print("\t1.Convert meters to miles")
    print("\t2.Convert miles to meter")
    print("\t3.Exit")

def meters_to_miles(x):
    y = x / 1609.344
    print(x,"miles equals", y,"meters.")

def miles_to_meters(y):
    x = y * 1609.344
    print(y,"meter equals", x,"miles.")

#main code
display_menu()
choice = int(input())
while choice != 3:
    n = int(input("Enter distance:"))
    if choice == 1:
        meters_to_miles(n)
    else:
        miles_to_meters(n)

    display_menu()
    choice = int(input())
        
    
