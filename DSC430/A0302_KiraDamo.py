#Written by Kira Damo
#I have not given or received any unauthorized assistance on this assignment
#Submitted April 27th
#https://youtu.be/Wr3fLqAx0LU

def sum_squares(n):
    '''formula for sums of squares. divides n into digits and adds them via accumulator'''
    sums = 0
    while (n != 0):
        d = n % 10
        sums += d ** 2
        n = n // 10
    return sums

def main():
    '''stores sums of squares in a dictionary where input number is a key and items are the status and sum of squares.
if user enters invalid answer for number, error will occur.'''
    results = {}
    while True:
        user_input=input('Enter a positive number or "end" to exit: ')
        if user_input.lower() == 'end':
            break
        try:
            num=int(user_input)
            if num <= 0:
                print('Please enter a positive number greater than 0.')
                continue         
        except ValueError:
            print('Invalid input. Please enter an integer')
            continue

        sequence = []
        seen = set()
        n = num
        while n != 1 and n not in seen:
            seen.add(n)
            sequence.append(n)
            n=sum_squares(n)
        sequence.append(n)
            
        if n == 1: 
            results[num] = ("happy", sequence)
            print(f"{num} is a happy number: {sequence}")
        else:
            results[num] = ('sad', sequence)
            print(f"{num} is a sad number: {sequence}")

    print('\nSumming up the results:')
    for num, result in results.items():
        print(f"{num}: {result}")
    
    
main()
