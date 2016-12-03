def format(i):
    alpha = "^_^_^"
    i = "i"
    space = " "
    for index in range(0,4):
        print(alpha,end='')
    print('')
    for indexa in range(0,4):
        for index2 in range(0, 5):
            print(i,end='    ')
        print('')
    if i==3:
        for index in range(0, 4):
            print(alpha, end='')

for lol in range(0,4):
    format(lol)