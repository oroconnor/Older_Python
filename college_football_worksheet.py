
yards_gained= {"2016":423.1, "2017":411.1,"2018":402.1}
print(yards_gained["2016"])
for key in yards_gained:
    print(key)
    print(yards_gained["2016"])

teams = {
    "LSU":{"Yards Gained":{"2016":423.1 , "2017":411.1,"2018":402.1}, "Yards Allowed":{"2016": 323.0, "2017":311.7,"2018":346.1}},
    "OU":{"Yards Gained":{"2016": 554.8, "2017":579.6,"2018":570.3}, "Yards Allowed":{"2016": 439.8, "2017":384.8,"2018":448.1}},
    "Clemson":{"Yards Gained":{"2016": 503.7, "2017":429.6,"2018":527.2}, "Yards Allowed":{"2016": 313.9, "2017":277.9,"2018":276.7}},
    "Ohio State" : {"Yards Gained":{"2016": 459.2, "2017":506.0,"2018":535.6}, "Yards Allowed":{"2016": 282.3, "2017":292.3,"2018":400.3}}
    }

yg = teams["LSU"["Yards Gained"["2016"]]]

print(yg)
