import string
import random
alphabet = string.ascii_lowercase
ALPHABET = string.ascii_uppercase
print("This program generates a random word.\nHere it is:")
random_word =   ALPHABET[random.randrange(26)]  + \
                alphabet[random.randrange(26)]  + \
                alphabet[random.randrange(26)]  + \
                alphabet[random.randrange(26)]  + \
                alphabet[random.randrange(26)]
print(random_word)
