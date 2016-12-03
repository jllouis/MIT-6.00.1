# guessing

minimum = 0
maximum = 100
guess = 0
answer = ''

print("Think of a number between 0 and 100!")
while True:
    guess = int((minimum+maximum)/2)
    print("Is your secret number: " +str(guess)+"?")
    answer = input("Low: l, High: h, or correct: ")
    if answer == 'l':
        minimum = guess
    elif answer == 'h':
        maximum = guess
    elif answer == 'c':
        print("Game over. Your secret number is: " + str(guess))
        break
    else:
        print("I did not understand your response")
        continue

