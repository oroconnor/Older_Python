import math
currency = ["British Pound Sterling","Euro","Canadian Dollar","Australian Dollar"]
rate = [[1.320,1.321,1.332,1.331,1.341],[1.143,1.156,1.138,1.122,1.129],[.757,.764,.760,.750,.749],[.720,.725,.729,.736,.739]]
x = float(input("Please enter an amount in U.S. Dollars for conversion:"))
for i in range(4):
    avg = math.fsum(rate[i]) / 5
    print(x,"U.S. Dollars =", x * avg, currency[i])
    
   
