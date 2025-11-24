#homework six problem 1

def contacts():
    phonebook={}
    while True:
        first_name = input('Enter first name: ')
        if not first_name:
            break
        else:
            last_name = input('Enter last name: ')
            person = (first_name, last_name)
            
            number = input('Enter 10-digit phone number: ')
            phone_number='{}-{}-{}'.format(number[:3], number[3:6], number[6:])

            phonebook[person].add(phone_number)
            
            if person in phonebook:
                print(first_name+' '+last_name+' has phone number(s) ', phone_number)
                phonebook[person] = {phone_number}
    return
