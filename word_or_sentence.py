count = 0
message = input("Please input a message:")
for i in message:
    if i == " ":
        count +=1
    if count >= 1: break
if count == 0:
    print("Your message had just one word.")
else:
    print("Your message had more than one word in it.")
