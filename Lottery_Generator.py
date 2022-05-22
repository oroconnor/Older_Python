import random
print("Welcome to the Lottery Generator")
draw_number = input("How many numbers are drawn for your lottery?:")
range_number = input ("OK. What is the highest number that might be drawn for each number? For example, if only the numbers 0-9 are being drawn, you would say '9.' If numbers 0-99 are drawn for each number, you would answer '99.' So, what is the highest number that might be drawn for each number?")
print("OK. Here are your lucky numbers:")
counter = 0
while counter < int(draw_number):
      number = random.randint(0,int(range_number))
      print(number)
      counter += 1
outcomes_number = ((int(range_number) + 1)) ** int(draw_number)
percentage_chance = (1 / outcomes_number) * 100
print("If the number being drawn all have equal probability of being drawn, and are drawn with replacement, your chances of winning this lottery are 1 in", outcomes_number)
print("aka", percentage_chance, "%")
