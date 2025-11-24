#Written by Kira Damo
#Submitted April 26th
#I have not given or received any unauthorized assistance on this assignment
#https://youtu.be/sUAXFM1qoIA

def prime_check(n):
    '''This function checks if number is prime all prime numbers under 100
are odd and cannot be divisible by 3, 5, and 7'''
    if n <= 1:
        return False
    if n <= 3:
        return True #2 and 3 are prime but 1 is not
    if n % 2 == 0 or n % 3 == 0 or n % 7 == 0:
        return False

    i = 5 #first number after non-prime number
    while i * i <= n:
        if n % i == 0 or n % (i + 1) == 0:
            return False
        i += 1 #accumulator
    return True
    
def goldbach_conjecture(value):
    '''Every integer greater than 2 is the sum of two prime numbers.
We must test for the number to be even and find two prime numbers that
add up to that prime number'''
    
    if value < 4 or value > 100: #cannot be completed if not within valid bounds
        print('Goldbach Conjecture cannot be completed. Please try again with a value that is between 4 and 100.')
    
    for n in range(4, value+1):
        for i in range(2, n // 2 + 1): #finds the prime numbers that get added
            if n % 2 == 0 and prime_check(i) == True and prime_check(n-i) == True:
                print('{}={}+{}'.format(n, i, n-i))
                break
        
