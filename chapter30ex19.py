nums = []
total = 0
for i in range(8):
    x = int(input("Please enter a number:"))
    nums.append(x)
for j in nums:
    if j > 0:
        total += j
print("The sum of the positive numbers entered is", total)
