#Assume s is a string of lower case characters.
#Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring.
# For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc
# Note: This problem may be challenging. We encourage you to work smart.
#  If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course.
#  If you have time, come back to this problem after you've had a break and cleared your head.

s = 'azcbobobegghakl'

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
longest = 0
lString = ''

for l in range(len(s)): # for every letter in the string
    currentLength = 1   # keeps track of the current length of the in-order string
    index = 0
    p = s[l]

    if (l + index + 1 == len(s)):
        break

    while (letters.index(s[l+index]) <= letters.index(s[l+index+1])):
        currentLength += 1
        index+=1
        p += s[l+index]
        #print("Current string: " + p)
        if (l+index+1 == len(s)):
            break

    if len(p) > longest:
        longest = currentLength
        lString = p

print("Longest substring in alphabetical order is: " + lString)