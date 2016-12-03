
def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    #start with exponent = 0, then increase it during each iteration
    exp = 0
    #calculate the difference between the base^exp to check to see if subsequent exponents approach or diverge from current
    diff = abs((base**exp) - num)
    #while the difference is approaching the number, keep going, if it is getting further from it, stop, the previous was the closest
    while (True):
        exp+=1
        newDiff = abs((base**exp) - num)

        if(newDiff >= diff):
            return exp-1

print(closest_power(2,192))



