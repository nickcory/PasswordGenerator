import random

lowerLetters = "abcdefghijklmnopqrstuvwxyz"
upperLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_-+={}[]|\;:,.<>/?\"\'"

print("Password Options: 1 - Letters, 2 - Letters and Numbers, 3 - Letters, Numbers and Symbols")
choice = int(input("Enter Number for Choice: "))

if choice == 1:
    allChar = upperLetters + lowerLetters
elif choice == 2:
    allChar = upperLetters + lowerLetters + numbers
elif choice == 3:
    allChar = upperLetters + lowerLetters + numbers + symbols



# allChar = lowerLetters + upperLetters + numbers + symbols
pass_len = int(input("Enter length for password: "))
password = "".join(random.sample(allChar, pass_len))

print("\nYour password is \n \n" + password + "\n")
