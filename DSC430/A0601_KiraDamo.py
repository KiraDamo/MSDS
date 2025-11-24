#Written by Kira Damo
#Submitted May 18th
#I have not given or received any unauthorized assistance on this assignment.
#https://youtu.be/anToB-EeQd8

def palindrome(date):
    'tests if dates are palindromes'
    date = date.replace('/', '')
    if date == date[::-1]:
        return True
    else:
        return False

def main():
    'finds the dates that are palindrome dates and writes them to a txt file'
    months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    file = open('palindrome.txt', 'w')

    for year in range(2000, 2100):
        for month in range(1,13):
            for day in range(1, months[month] + 1):
                if day < 10 and month < 10:
                    date = '0{}/0{}/{}'.format(day, month, year)
                elif day < 10 and month >= 10:
                    date = '0{}/{}/{}'.format(day, month, year)
                elif day >= 10 and month < 10:
                    date = '{}/0{}/{}'.format(day, month, year)
                else:
                    date = '{}/{}/{}'.format(day, month, year)

                if palindrome(date) == True:
                    file.write(date)
                    file.write('\n')

    file.close()
