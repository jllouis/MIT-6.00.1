#given values
balance = 4473
annualInterestRate = .2
#submission starts here
monthlyInterestRate = annualInterestRate/12.0

found = False
minRange = 0
maxRange = balance

while not found:
    cRate = (minRange+maxRange)/2.0
    remaining = balance

    for i in range(0,12):
        remaining -= cRate
        remaining += remaining*monthlyInterestRate

    if (round(remaining,2) < 0.2):
        maxRange = cRate
    elif (round(remaining,5) > 0.2):
        minRange = cRate
    else:
        found = True
    print("remaining:  "+str(remaining))

print("Lowest payment: "+str(round(cRate,0)))
#END PROGRAM