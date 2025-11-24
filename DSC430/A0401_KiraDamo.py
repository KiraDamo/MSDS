#Written by Kira Damo
#submitted May 3rd, 2025
#I have not given or received any unauthorized assistance on this assignment
#https://youtu.be/-sx30u31r8E

def goldenbach_deuce():
    '''Accepts a num and a length from user. Program finds two numbers from the randomly curated
list of numbers from 0 to 100 that add to the sum.'''
    import random
    sum = input('Please enter a sum: ')
    sum = int(sum)
    length = input('Please enter a length: ')
    length = int(length)

    num_list=[] # creates list of randomly generated numbers
    for i in range(0,length):
      num = random.randrange(0,100)
      num_list.append(num)

    num_list.sort() 
    low = 0 #range in which numbers are found
    high = length-1

    print('\nList: '+str(sorted(num_list)))
    
    while low < high:
        if sum == num_list[low] + num_list[high]: 
            print('\nFound a pair! {}={}+{}'.format(sum, num_list[low], num_list[high]))
            break
        elif sum > num_list[low] + num_list[high]: #adjusts to find pair as needed
            low += 1
        elif sum < num_list[low] + num_list[high]:
            high -= 1
    return
