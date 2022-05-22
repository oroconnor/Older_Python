


print("Welcome to the Mortgage Calculator!")
loan_amnt = int(input("What is your initial mortgage balance?"))
interest_rt = float(input("What is your interest rate?"))
term_lnth= int(input("How many years is the term of the loan?"))
payment = int(input("What is your monthly payment?"))
loan_months = term_lnth * 12
total_interest = 0
month = 1
current_bal = loan_amnt
mortgage_sched = []

#print("Here is your amortization schedule without any extra payments:")
while month <= loan_months:
    inter_pay = (current_bal * interest_rt)/12
    prin_pay = payment - inter_pay 
    #print("Month ", month, " : Principal payment =  ", prin_pay, " Interest payment = " , inter_pay ," Loan Balance = ", current_bal)
    current_bal  -= prin_pay
    month += 1
    total_interest += inter_pay

print("Over the life of the loan you will pay ", total_interest, "in interest!")

total_interest_alt = 0
month = 1
current_bal = loan_amnt
extra = int(input("How much of an extra payment are you going to make each month?"))
print("Here is your amortization schedule your month extra payments of ",extra, ":")        
while month <= loan_months and current_bal >= 0:
    inter_pay = (current_bal * interest_rt)/12
    prin_pay = (payment - inter_pay) + extra
    #print("Month ", month, " : Principal payment =  ", prin_pay, " Interest payment = " , inter_pay ," Loan Balance = ", current_bal)
    current_bal  -= prin_pay
    month += 1
    total_interest_alt += inter_pay
    mortgage_sched.append(current_bal)
inter_dif = total_interest - total_interest_alt
early = (loan_months - month) / 12
print("With the extra payment, over the life of the loan you will pay ", total_interest_alt, "in interest!")
print("By adding the extra monthly payment of ", extra, " you will save ", inter_dif, "! Wow!")
print("You will have your loan paid off by month ", month,", which is ",early," years early than your original schedule! Not too shabby!")

while 5 <= 10:
    query_month = int(input("If you want to see the loan balance for your mortgage at a particular month (with the extra principal payments), please input the month number now (for example, '136'):"))-1
    print(mortgage_sched[query_month])
    
