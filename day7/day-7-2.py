import random

word_list = ["hello", "world", "python"]

chosenWord = random.choice(word_list)
display = ['_' for x in chosenWord]

print(chosenWord)
print(display)

guess = input("Guess a letter: ").lower()

for i in range(len(chosenWord)) :
    if chosenWord[i] == guess :
        display[i] = guess

print(display)


