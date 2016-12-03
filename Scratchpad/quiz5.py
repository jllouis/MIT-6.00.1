def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    #keep track of running sum
    sum = 0

    for i in range(0,len(listA)):
        sum+=(listA[i]*listB[i])
    return sum

print(dotProduct([1,2,3],[4,5,6]))