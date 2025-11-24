#Written by Kira Damo
#Indicating which letter occurs more often in the txt file

def play(num):
    fname = 'Pride_and_Prejudice.txt'
    infile = open(fname, 'r')
    s=infile.read()
    infile.close()
   
    for i in range(num):
        import random
        isValid=True
        sLetters = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
        letterChoice1 = random.choice(sLetters)
        letterChoice2 = random.choice(sLetters)
        answer = input('Which letter occurs more often? "'+ letterChoice1 + '" or "'+ letterChoice2 + '"? ')
        choice1Count=s.count(letterChoice1)
        choice2Count=s.count(letterChoice2)

        if letterChoice1 == letterChoice2:
            isValid = False
            print('The letters are the same\n  ','"'+letterChoice1+'"',' occurs ', choice1Count, 'times')
        elif answer not in sLetters:
            print('"'+answer+'"'+' is not a letter.')
            
        elif answer == letterChoice1:
            if choice1Count > choice2Count:
                print('Correct: ', letterChoice1, ' occurs ',choice1Count, ' times and ', letterChoice2, ' occurs ', choice2Count, ' times.')
            else:
                    print('Incorrect: ', letterChoice1, ' occurs ', choice1Count, ' times and ', letterChoice2, ' occurs ', choice2Count, ' times.')
        elif answer == letterChoice2:
            if choice2Count > choice1Count:
                print('Correct: ', letterChoice1, ' occurs', choice1Count, ' times and ', letterChoice2, ' occurs ', choice2Count, ' times.')
            else:
                print('Incorrect: ', letterChoice1, ' occurs ', choice1Count, ' times and ', letterChoice2, ' occurs ', choice2Count, ' times.')

        if answer != letterChoice1 and answer != letterChoice2:
            print('"'+answer+'" is not one of the choice letters.')

    print('Goodbye')
