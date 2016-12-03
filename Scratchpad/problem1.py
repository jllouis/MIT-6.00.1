balance = 42
annualInterestRate = .2
monthlyPaymentRate = .04

monthlyInterestRate = annualInterestRate/12.0
minimumPayment = monthlyPaymentRate*balance

for i in range(0,12):
    balance -= monthlyPaymentRate*balance
    balance += balance*monthlyInterestRate

print("Month "+str(i)+ " remaining balance: "+str(round(balance,2)))
