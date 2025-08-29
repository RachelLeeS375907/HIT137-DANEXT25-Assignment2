#Define encryption function.
def encryptText(unencryptedText, alphaLowerFirst, alphaLowerSecond, alphaUpperFirst, alphaUpperSecond, key1, key2, key3, key4):
    encryptedText = ""
    for char in unencryptedText:
        ordvalue = ord(char)
        if char in alphaLowerFirst:
            newCharacter = ord(char) + key1
            encryptedText += chr(((newCharacter - ord('a')) % 26) + ord('a'))
        elif char in alphaLowerSecond:
            newCharacter = ord(char) - key2
            encryptedText += chr(((newCharacter - ord('a')) % 26) + ord('a'))
        elif char in alphaUpperFirst:
            newCharacter = ord(char) - key3
            encryptedText += chr(((newCharacter - ord('A')) % 26) + ord('A'))
        elif char in alphaUpperSecond:
            newCharacter = ord(char) + key4
            encryptedText += chr(((newCharacter - ord('A')) % 26) + ord('A'))
        else:
            encryptedText += char
    return encryptedText

#Define decryption function.
def decryptText (encryptedText, alphaLowerFirst, alphaLowerSecond, alphaUpperFirst, alphaUpperSecond, key1, key2, key3, key4):
    decryptedText = "" 
    for char in encryptedText:
        if char in alphaLowerFirst:
            newCharacter = ord(char) - key1
            if newCharacter < ord('a'):
                newCharacter = ord('z') - (ord('a') - newCharacter - 1)
            decryptedText += chr(((newCharacter - ord('a')) % 26) + ord('a'))
        elif char in alphaLowerSecond:
            newCharacter = ord(char) + key2
            if newCharacter > ord('z'):
                newCharacter = ord('a') + (newCharacter - ord('z') - 1)
            decryptedText += chr(((newCharacter - ord('a')) % 26) + ord('a'))
        elif char in alphaUpperFirst:
            newCharacter = ord(char) + key3
            if newCharacter < ord('A'):
                newCharacter = ord('Z') + (newCharacter - ord('Z') - 1)
            decryptedText += chr(((newCharacter - ord('A')) % 26) + ord('A'))
        elif char in alphaUpperSecond:
            newCharacter = ord(char) - key4
            if newCharacter < ord('A'):
                newCharacter = ord('Z') - (ord('A') - newCharacter - 1)
            decryptedText += chr(((newCharacter - ord('A')) % 26) + ord('A'))
        else:
            decryptedText += char
    return decryptedText

#Define decryption verification function.
def verDecryption(decryptedText, unencryptedText):
    if decryptedText == unencryptedText:
        print("Decryption succesful!")
    else:
        print("Decryption unsuccessful.")

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

#Open and read from text file "raw_text.txt".
with open("raw_text.txt", 'r') as inputFile:
    unencryptedText = inputFile.read()

#Call encryption function to encrypt text from "raw_text.txt".
encryptedText = encryptText(unencryptedText, alphaLowerFirst, alphaLowerSecond, alphaUpperFirst, alphaUpperSecond, key1, key2, key3, key4)

#Write encrypted text to new file "encrypted_text.txt" and close.
with open("encrypted_text.txt", 'w') as outputFile:
    outputFile.write(encryptedText)
outputFile.close()

#Open and read from text file "encrypted_text.txt".
with open("encrypted_text.txt", 'r') as encyptedFile:
    encryptedInput = encyptedFile.read()

#Call decryption function to decrypt text from file.
decryptedText = decryptText(encryptedText, alphaLowerFirst, alphaLowerSecond, alphaUpperFirst, alphaUpperSecond, key1, key2, key3, key4)

#Call decryption verification function to verify whether decryption successful.
decryptionResult = verDecryption(decryptedText, unencryptedText)