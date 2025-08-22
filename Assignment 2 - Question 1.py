"""Create a program that reads the text file "raw_text.txt", encrypts its contents using a simple 
encryption method, and writes the encrypted text to a new file "encrypted_text.txt". 
Then create a function to decrypt the content and a function to verify the decryption was successful."""

#Open and read from text file raw_text.txt.
with open("raw_text.txt", 'r') as inputFile:
    unencryptedText = inputFile.read()

#Define separate parts of alphabet to allow for different encryption
alphaLowerFirst = "abcdefghijklm"
alphaLowerSecond = "nopqrstuvwxyz"
alphaUpperFirst = "ABCDEFGHIJKLM"
alphaUpperSecond = "NOPQRSTUVWXYZ"

#Enter first number for encryption key
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
    
#Enter second number for encryption key
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


