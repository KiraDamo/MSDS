#written by kira Damo
#calculating the student loan amount
#csv file must print payment number, payment, interest, principal, balance, total interest
#convert anual to monthly

def student_loan(amount,rate,years):
    outfile = open('student_loan.csv', 'w')
    outfile.write('Prepared by: Kira Damo\n')
    formatTitles = '{},{},{},{},{},{}'.format('Payment Number','Payment','Interest','Principal','Balance','Total Interest')
    outfile.write(formatTitles+'\n')
    months = years * 12
    interestRate = (rate / 100) / 12
    principal = 0
    Totinterest = 0
    total = 0
    paid = 0
    balance = amount
    interest = 0
    
    for i in range(1,months+1):
        monthlyPayment = (interestRate * amount) / (1-(1+interestRate)**(-months))
        interest = interestRate * balance
        balance = balance - monthlyPayment + interest
        paid = paid + monthlyPayment
        Totinterest = Totinterest + interest
        principal = monthlyPayment - interest

        formatStr = '{:2},{:.2f},{:.2f},{:.2f},{:.2f},{:.2f}'.format(i,monthlyPayment,interest,principal,balance,Totinterest)
        outfile.write(formatStr+'\n')

        
    lstr = '''If you had ${:,.2f} in student loans at {}% and a {}-year term, your monthly
payments would be ${:,.2f}. Over the life of your loan, you would repay a total
of ${:,.2f}; interest charges would cause your balance to grow by ${:,.2f}.'''
        
    print('Student Loan Summary\n\n'+lstr.format(amount, rate, years, monthlyPayment, amount+Totinterest, Totinterest))

    print('''\nTo view monthly detail go to student_loan.csv
Thanks for using the student_loan() function.''')














    

