"""This program screens long jumpers for Olympic Qualification."""
import statistics
distance1 = int(input("What is your first long jump length?"))
distance2 = int(input("What is your second long jump length?"))
distance3 = int(input("What is your third long jump length?"))
distances = [distance1,distance2,distance3]
avgdistance = statistics.mean(distances)
if avgdistance >= 8:
    print("Congrats! You qualify for the Olympics!")
else:
    print("I'm so sorry. You don't qualify for the Olympics!")
print("Your average long jump distance was ", avgdistance)
