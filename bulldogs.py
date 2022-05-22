import datetime as dt
import random

class Bulldogs:
    life_expectancy_days = dt.timedelta(days = 3650)
    birthday = dt.date.today()
    expected_death = birthday + life_expectancy_days 
    def __init__(self, name, wght): 
        self.dogname = name
        self.weight = wght
       
most_pop_dognames = {"luna","coco","charlie","daisy","lucy","bailey","buddy","rocky"}

for dog in most_pop_dognames:
    birth_weight = random.randint(2,9)
    dog = Bulldogs(dog, birth_weight)
    print((dog.dogname).title())
    print(dog.weight, "lbs")
    print(dog.birthday)
    print(dog.expected_death)
    
with open("french_bulldogs.txt","r") as f:
    frenchies = f.read().splitlines()
    print(frenchies)

class French(Bulldogs):
    life_expectancy_days = dt.timedelta(days = 4380)
   
for dog in frenchies:
    birth_weight = random.randint(2,9)
    dog = French(dog, birth_weight)
    print((dog.dogname).title())
    print(dog.weight, "lbs")
    print(dog.birthday)
    print(dog.expected_death)
