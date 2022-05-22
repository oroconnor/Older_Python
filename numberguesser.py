import random
x = random.randint(1,100)
counter = 0
y = int(input("Guess the secret number:"))
while True:
    counter +=1
    if y < x:
        y = int(input("Your guess is smaller than the secret number. Guess again:"))
    elif y > x:
        y = int(input("Your guess is larger than the secret number. Guess again:"))
    else: break
       
print("You found it! It took", counter, "guesses!")
