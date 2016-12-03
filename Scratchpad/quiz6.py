import math

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    # Your code here
    for element in L:
        if (type(element) == type(L)): #if the type of  the elements are the same type of the parent: recurse!
            deep_reverse(element)
        listLength = math.floor(len(L)/2)
        for i in range (0, listLength):
            temp = L[listLength - i]
            L[i] = L[listLength - i]
            L[listLength - 1] = temp
        return L
    return L


L = [[1, 2], [3, 4], [5, 6, 7]]
print(deep_reverse(L))