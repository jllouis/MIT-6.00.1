#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print
#Number of times bob occurs is: 2

s = 'bobbbobbobobomoqbobbddwbobbobb'
numbob = 0
for l in range(len(s)):
    if (l+2 == len(s)):
        break
    if s[l] == 'b' and s[l+1] == 'o' and s[l+2] == 'b':
        numbob += 1
print("Number of times bob occurs is: " +str(numbob))
