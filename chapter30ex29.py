nums = []
total = 0
for i in range(10):
    x = int(input("Please enter a number:"))
    nums.append(x)
for j in nums:
    if j % 2 == 0:
        total += nums[j]

print("Total of the values with even indices:", total)
