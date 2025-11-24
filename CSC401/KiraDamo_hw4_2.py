#Written by Kira Damo
#shifting letters to encrypt a message
#must keep spaces and punctuation

def Caesar(message,shift):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    message=message.upper()
    cipher = alphabet[shift: ]+alphabet[ :shift]
    encryptedMsg=''
    for letter in range(len(message)):
        if message[letter] == '':
            encryptedMsg += ''
        if message[letter] not in alphabet:
            encryptedMsg += message[letter]
        else:
            alphabetindex=alphabet.index(message[letter])
            newindex=(alphabetindex + shift) % len(alphabet)
            newletter=alphabet[newindex]
            encryptedMsg += newletter
    print('alphabet: '+alphabet)   
    print('cipher: '+cipher)
    return encryptedMsg

    
def main():
    message = input('Enter message: ')
    shift = int(input('Enter shift amount: '))
    encryptedMsg = Caesar(message, shift)
    print(message)
    print(encryptedMsg)
