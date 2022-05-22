product = 1
total = 0
print("Please enter 10 numbers...")
for x in range(0,10):
    i = float(input("Enter a number:"))
    product = i * product
    total = i + total
print("The product of all 10 numbers is:",product)
print("The average value of all 10 numbers is:", total / 10)
              
