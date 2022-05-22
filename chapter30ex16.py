nums = []
for i in range(8):
    x = int(input("Enter a number:"))
    nums.append(x)
for num in range(8):
    nums[num] **= 2
for j in nums[::-1]:
    print(j)
    
