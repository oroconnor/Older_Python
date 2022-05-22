def num_of_days(year,month):
    thirtyonemonths = [1,3,5,7,8,10,12]
    thirtymonths = [4,6,9,11]
    if month in thirtyonemonths:
        days = 31
    elif month in thirtymonths:
        days = 30
    else:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            days = 28
        else:
            days = 29
    return days

#main code
year = int(input("Please enter the year:"))
month = int(input("Please enter the month:"))

x = num_of_days(year,month)

print("There are,", x,"days in month",month,"of the year",year,".")
    
