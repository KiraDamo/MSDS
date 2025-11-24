#Written by Kira Damo

def startUp():
    accounts = {}
    fname = 'accounts.csv'
    infile = open(fname, 'r')
    cx=infile.readlines()
    for i in range(len(cx)):
        cx[i] = cx[i].split(',')
        pin = int(cx[i][0])
        firstName = cx[i][1]
        lastName = cx[i][2]
        balance = cx[i][3]
        accounts[pin] = [firstName, lastName, float(balance)]            
    return accounts

      
def verifyPin(d):
    d = startUp()
    count = 2
    entry = False
    pin = int(eval(input('Please enter your 4-digit PIN: ')))
    msg = "Please call customer support at 800-000-0000"
    while count > 0 and entry == False:
        if pin in d.values()==False:
            pin = input('Invalid pin, try again: ')
            count -= 1
        else:
            entry = True
            return(pin, d[pin][0])
    if count == 0:
        return(None, msg)

def verifyMenuChoice():
    choice = input('Enter choice: ')
    while choice != 1 or 2 or 3 or 4:
        try:
            choice = int(choice)
            if choice in [1,2,3,4]:
                return choice
            else:
                choice = input("Enter 1 or 2 or 3 or 4, try again.")
        except ValueError:
            choice = input("X invalid choice, non-numeric characters not allowed, try again: ")

    
def displayMenu(name):
    print(name ,': \n 1. Deposit\n 2. Withdrawal\n 3. Balance\n 4. Quit\n')
    choice = verifyMenuChoice()
    return choice

def verifyAmount():
    entry = input("Amount: ")
    try:
        choice = float(entry)
        while choice < 0 :
            choice = float(eval(input("Negative amount. Try again: ")))
    except ValueError:
        choice = float(eval(input("Invalid amount. Use digits only: ")))
    return choice

def deposit(pin, d):
    amount = verifyAmount()
    balance = d[pin][2] + amount
    d[pin] = [d[pin][0],d[pin][1],balance]
    return

def withdraw(pin, d):
    amount = verifyAmount()
    balance = d[pin][2]
    while True:
        if amount > balance:
            print('Insufficient funds to complete transaction. Try again.')
            amount=verifyAmount()
        else:
            balance = d[pin][2] - amount
            d[pin][2] = balance
            break
    return

def balance(pin, d):
    print('Current balance is ${:.2f}'.format(d[pin][2]))
    return d[pin][2]
    
def quit(pin, d):
    response=''
    while response != 'y' or 'n':
        response = (input('Are you sure you want to quit? y/n '))
        response = response.lower()
        if response == 'y':
            receipt(pin, d)
            break
        elif response == 'n':
            return response
            break
        else:
            response = input('Invalid Response. Are you sure you want to quit? y/n ')
            response = response.lower()

def receipt(pin, d):
    from datetime import date
    date= date.today()
    print('ABC Bank Branch Receipt\n   123 Bank St.\n   Anytown, USA\n')
    print('Date: '''+str(date)+' \nName: ' + d[pin][0], d[pin][1] +'\nAvailable Balance: $'+ str(d[pin][2])+' \n\nThank you for using the ABC Banking System')
    #print("'Goodbye'") returned in tester so I commented it out
    return 
        
            
        
def tester():
    dict = startUp() #dictionary
    print()
    if dict == None:
        return
    pin,msg = verifyPin(dict)
    if pin == None:
        print(msg)
        return 'Goodbye'
    name = msg

    while True:
        print()
        choice = displayMenu(name)
        if choice == 1:
            deposit(pin, dict)
        elif choice == 2:
            withdraw(pin, dict)
        elif choice == 3:
            b = balance(pin, dict)
            msg = 'Current balance is ${:,.2f}'
            print('\n',msg.format(b))
        elif choice == 4:
            reply = quit(pin, dict)
            if reply == 'n':
                pass
            else:
                return 'Goodbye'
    return
        
        
    
