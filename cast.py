a = input("Enter a number:")
b = input("Now enter another number:")

sum = a + b
print("\nData Type sum:", sum, type(sum))
sum = int(a) + int(b)
print("Data Type sum:", sum, type(sum))
sum = float(sum)
print("Date Type sum:", sum, type(sum))
sum = chr(int(sum))
print("Date Type sum:", sum, type(sum))