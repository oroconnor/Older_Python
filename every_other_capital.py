word = str(input("Please enter a six letter word with every other letter capitalized."))
if (word[0::2] == word[0::2].upper() and word[1::2] == word[1::2].lower()) or (word[0::2] == word[0::2].lower() and word[1::2] == word[1::2].upper()):
    print("Every other letter IS capitalized!")
else:
    print("Every other letter IS NOT capitalized!")
