n = int(input("How many integers would you like to enter?"))
count = 0
for j in range(n):
    x = int(input("Enter an integer, please:"))
    if x % 2 == 0:
        count += 1
if count == 0:
    print("You entered no even integers.")
else:
    print("You entered",count,"even integers.")
