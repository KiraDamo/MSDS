#Written By Kira Damo
#Submitted May 10
#I have not given or received any unauthorized assistance on this assignment
#https://youtu.be/OGkGzrBNQgc

import random
from A0501_KiraDamo import SixSidedDie, TenSidedDie, TwentySidedDie, Cup

def rolling_game():
    print('Hello! This is the rolling game!')
    name = input("Please enter your name: ")
    score = 0

    while True:
        goal = random.randint(1,100)
        
        try:
            six_n = int(input('How many 6-sided dice would you like to roll to get to {}? '.format(goal)))
            ten_n = int(input('How many 10-sided dice would you like to roll to get to {}? '.format(goal)))
            twenty_n = int(input('How many 20-sided dice would you like to roll to get to {}? '.format(goal)))
        except ValueError:
            print('Please enter an integer.')
            continue
        
        cup = Cup(six_n, ten_n, twenty_n)
        rolled = cup.roll()

        print('The sum of your rolls is {}'.format(cup.getSum()))

        difference = goal - rolled

        if difference == 0:
            score += 10
        elif difference > 0 and difference <= 3:
            score +=5
        elif difference > 3 and difference <= 10:
            score += 2

        print('Results for {}'.format(name))

        print('The goal was {}, and you rolled a {}. Your current score is {}'.format(goal, rolled, score))

        play=input('Would you like to play again? (yes/no) ').lower()
        if play == 'no':
            print('Thanks for playing! Your final score is {}'.format(score))
            break

        
