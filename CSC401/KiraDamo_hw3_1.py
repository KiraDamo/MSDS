#written by Kira Damo
#formatting outputs to be in 3 columns

def formatOutput(num):
    import random
    lst = []
    for i in range(num):
        lst.append(random.uniform(0,10000))

    for i in range(num // 3):
        print('{0:8,.2f}     {1:8,.2f}     {2:8,.2f}'.format(lst[i*3], lst[i*3+1], lst[i*3+2]))
    if num % 3 == 2: #two values in last row
        print('{0:8,.2f}     {1:8,.2f}'.format(lst[-2], lst[-1]))
    if num % 3 == 1: #one value in last row
        print('{0:8,.2f}'.format(lst[-1]))
    return
