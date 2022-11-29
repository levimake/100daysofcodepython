import string
import random

def getList(s):
    return list(filter(lambda i:(i in s),s))

def getSeq(myList, length):
    return [myList[random.randint(0, len(myList)-1)] for x in range(length)]

letters = getList(string.ascii_letters)
numbers = getList(string.digits)
symbols = getList(string.punctuation)

print("Welcome to PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = []
password += (getSeq(letters, nr_letters))
password += (getSeq(symbols, nr_symbols))
password += (getSeq(numbers, nr_numbers))

random.shuffle(password)

pyPassword = ''.join([str(element) for element in password])

print(pyPassword)

