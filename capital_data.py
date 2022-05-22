name1 = input("Please enter the name of the first person:")
age1 = int(input("Please enter the age of the first person:"))
name2 = input("Please enter the name of the second person:")
age2 = int(input("Please enter the age of the second person:"))
name3 = input("Please enter the name of the third person:")
age3 = int(input("Please enter the age of the third person:"))
if age1 == min(age1, age2, age3):
    print(name1, "is the youngest person.")
elif age2 == min(age1, age2, age3):
    print(name2, "is the youngest person.")
else:
    print(name3, "is the youngest person.")
if age1 == max(age1, age2, age3):
    print(name1, "is the oldest person.")
elif age2 == max(age1, age2, age3):
    print(name2, "is the oldest person.")
else:
    print(name3, "is the oldest person.")
           
            
