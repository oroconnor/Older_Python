count = 0
message = input("Please input a message:")
for i in message:
    for j in range(10):
        if i == str(j):
            count += 1
        if count >= 1: break
if count == 0:
    print("Your message had no digits in it.")
else:
    print("Your message had at least one number digit in it!")

