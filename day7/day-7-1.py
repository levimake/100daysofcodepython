import random

word_list = ["hello", "world", "python"]

chosenWord = random.choice(word_list)

guess = input("Guess a letter: ").lower()

for letter in chosenWord:
    if letter == guess :
        print("Right")
    else :
        print("Wrong")



