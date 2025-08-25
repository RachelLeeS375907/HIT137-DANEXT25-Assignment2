#Open and read from text file "raw_text.txt".
with open("raw_text.txt", 'r') as inputFile:
    unencryptedText = inputFile.read()

#Define alphabet bands to allow for different shifts.
alphaLowerFirst = "abcdefghijklm"
alphaLowerSecond = "nopqrstuvwxyz"
alphaUpperFirst = "ABCDEFGHIJKLM"
alphaUpperSecond = "NOPQRSTUVWXYZ"

#Enter first shift for encryption.
while True:
    try:
        shift1 = int(input("Please enter a number: "))
        if shift1 >10:
            print("Please enter a lower number.")
        elif shift1 <0:
            print("Please enter a higher number.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")
    
#Enter second shift for encryption.
while True:
    try:
        shift2 = int(input("Please enter a number: "))
        if shift2 >10:
            print("Please enter a lower number.")
        elif shift2 <0:
            print("Please enter a higher number.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")

#Define keys for encryption and decryption
key1 = shift1 * shift2
key2 = shift1 + shift2
key3 = shift1
key4 = shift2 ** 2

#Encrypt text from "raw_text.txt".
encryptedText = ""
for char in unencryptedText:
    ordvalue = ord(char)
    if char in alphaLowerFirst:
        newCharacter = ord(char) + key1
        if newCharacter > ord('m'):
            newCharacter = ord('a') + key1 - (ord('m') - newCharacter + 1)
        encryptedText += chr(((newCharacter - ord('a')) % 26) + ord('a'))
    elif char in alphaLowerSecond:
        newCharacter = ord(char) - key2
        if newCharacter < ord('n'):
            newCharacter = ord('n') - key2 - (ord('z') - newCharacter + 1)
        encryptedText += chr(((newCharacter - ord('a')) % 26) + ord('a'))
    elif char in alphaUpperFirst:
        newCharacter = ord(char) - key3
        if newCharacter > ord('M'):
            newCharacter = ord('A') - key3 - (ord('M') - newCharacter + 1)
        encryptedText += chr(((newCharacter - ord('A')) % 26) + ord('A'))
    elif char in alphaUpperSecond:
        newCharacter = ord(char) + key4
        if newCharacter < ord('N'):
            newCharacter = ord('N') + key4 - (ord('Z') - newCharacter + 1)
        encryptedText += chr(((newCharacter - ord('A')) % 26) + ord('A'))
    else:
        encryptedText += char
        
#Write encrypted text to new file "encrypted_text.txt" and close.
with open("encrypted_text.txt", 'w') as outputFile:
    outputFile.write(encryptedText)
outputFile.close()

#Open and read from text file "encrypted_text.txt".
with open("encrypted_text.txt", 'r') as encyptedFile:
    encryptedInput = encyptedFile.read()