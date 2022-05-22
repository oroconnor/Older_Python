words =[]
for i in range(6):
    x = input("Please enter a word:")
    words.append(x)
for y in range(6):
    if len(words[y]) > 10:
        print(words[y])
