import random

a, b = 1, 99
userGuide = 0
while userGuide != "c":
    pcGuess = random.randint(a, b)
    print(pcGuess)
    userGuide = input("Enter your guidance: c for correct b if your number is bigger s if your number is smaller: ")
    if userGuide != "c":
        if userGuide == 'b':
            a = pcGuess
        elif userGuide == 's':

            b = pcGuess
        continue
    else:
        userGuide = 'c'
        print('correct')
        break