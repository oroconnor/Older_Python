nums = []
inds = []
for i in range(8):
    x = int(input("Please enter a number:"))
    nums.append(x)
    if x < 20:
        inds.append(i)
print("Here are the indices for the values that are less than 20:",inds)
    
