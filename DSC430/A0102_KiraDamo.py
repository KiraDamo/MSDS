#Written by Kira Damo
#Assignment 1 Question 2 due April 10th
#Submitted April 9th
#I have not given or received any unauthorized assistance on this assignment
#https://youtu.be/qfZmB6E-88o

def coprime(a,b):
    'calculates the greatest common denominator'
    while b != 0:
        c = a % b #cannot divide by 0 or else that would be undefined
        a = b
        b = c
    return a

    if a == 1:
        return True
    if a != 1:
        return False
    

def coprime_test_loop():
    'prints if the numbers are coprime and allows user to exit as needed.'
    while True:
        a = input("Please enter a number or press enter to cancel: ")
        if a == "":
            print("Thank you. Goodbye.")
            break
        else:
            a = int(a)
            
        b = eval(input("Please enter another number: "))

        coprime(a,b)

        if coprime(a,b) == True:
            print('{} and {} are coprime numbers.'.format(a,b))
        else:
            print('{} and {} are not coprime numbers'.format(a,b))
    
coprime_test_loop()
