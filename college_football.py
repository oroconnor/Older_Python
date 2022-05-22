


teams = {
    "LSU":{"Yards Gained":{"2016":423.1 , "2017":411.1,"2018":402.1}, "Yards Allowed":{"2016": 323.0, "2017":311.7,"2018":346.1}},
    "OU":{"Yards Gained":{"2016": 554.8, "2017":579.6,"2018":570.3}, "Yards Allowed":{"2016": 439.8, "2017":384.8,"2018":448.1}},
    "Clemson":{"Yards Gained":{"2016": 503.7, "2017":429.6,"2018":527.2}, "Yards Allowed":{"2016": 313.9, "2017":277.9,"2018":276.7}},
    "Ohio State" : {"Yards Gained":{"2016": 459.2, "2017":506.0,"2018":535.6}, "Yards Allowed":{"2016": 282.3, "2017":292.3,"2018":400.3}}
    }

print("Hello, this is a program that helps you filter college football teams based on their performance from 2016, 2017, and 2018.")
print("Maybe it will help you pick the winners for next year (but probably not).")
print("This program will filter the football teams based on two statistics, one offensive metric and one defensive metric: Average Yards Gained per Game, and Average Yards Allowed per Game")
print("You can input a value for each metric, and the program will return to you a list of the teams that meet or exceed your criteria.")

user_yg = int(input("Please input your filter criterion for Average Yards Gained per Game (suggested range of between 400-600): "))
user_ya = int(input("Please input your filter criterion for Average Yards Allowed per Game (suggested range of between 250-500): "))


print("The following teams meet your criterion for Average Yards Gained per Game:")
counter_1 = 0
for key in teams:
    counter = 0
    yg = teams[key]["Yards Gained"]["2018"]
    if yg >= user_yg:
        print(key)  
        counter_1 += 1
if counter_1 == 0:
    print("Sorry, no teams meet that criterion.")
        
print("The following teams meet your criterion for Average Yards Allowed per Game:")
counter_2 = 0
for key in teams:
    ya = teams[key]["Yards Allowed"]["2018"]
    if ya <= user_ya:
        print(key)
        counter_2  += 1
if counter_2 == 0:
    print("Sorry, no teams meet that criterion.")
    
print("The following teams meet both of your criteria:")
counter_3 = 0
for key in teams:
    ya = teams[key]["Yards Allowed"]["2018"]
    yg = teams[key]["Yards Gained"]["2018"]
    if ya <= user_ya and yg >= user_yg:
        print(key)
        counter_3  += 1
if counter_3 == 0:
    print("Sorry, no teams meet both criteria.")
