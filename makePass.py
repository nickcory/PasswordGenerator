import random

lowerLetters = "abcdefghijklmnopqrstuvwxyz"
upperLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_-+={}[]|\;:,.<>/?\"\'"

allChar = lowerLetters + upperLetters + numbers + symbols
pass_len = int(input("Enter length for password: "))
password = "".join(random.sample(allChar, pass_len))

print("\nYour password is \n \n" + password + "\n")
