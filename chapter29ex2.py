num = int(input("Please enter a number between 0 and 20:"))
print("Here are the numbers whose digits add up to less than the number to inputted:")
for i in range (999,10000):
    a,b = divmod(i,1000)
    b,c = divmod(b,100)
    c,d = divmod(c,10)
    if a + b + c + d < num:
          print(i)
    
