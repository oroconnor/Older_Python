name1 = input("Please enter the name of the first person:")
age1 = int(input("Please enter the age of the first person:"))
name2 = input("Please enter the name of the second person:")
age2 = int(input("Please enter the age of the second person:"))
name3 = input("Please enter the name of the third person:")
age3 = int(input("Please enter the age of the third person:"))

if age1 == min(age1, age2, age3):
   x = name1
   a = age1
elif age2 == min(age1, age2, age3):
    x = name2
    a = age2
else:
    x = name3
    a = age3
if age1 == max(age1, age2, age3):
    y = name1
    b = age1
elif age2 == max(age1, age2, age3):
    y = name2
    b = age2
else:
    y = name3
    b = age3
            
if age1 not in [a,b]:
    z = age1
elif age2 not in [a,b]:
    z = age2
else:
    z = age3

if z - a < b - z:
    print("The youngest is", x)
else:
    print("The oldest is", y)
