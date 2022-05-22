count = 0
total = 0
n = int(input("How many integers do you want to enter?"))
while count < n:
    x = int(input("Enter a number:"))
    total += x
    count += 1
print("Total sum of integers inputted is:",total)
print("Average of inputs is:", total / n)
