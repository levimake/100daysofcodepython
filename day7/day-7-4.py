from hangman_art import HANGMANPICS, HANGMAN_LOGO
from randomWords import getWord
from clear import clrscr

totalLives = len(HANGMANPICS)

import random

chosenWord = getWord()
display = ['_' for x in chosenWord]

print(HANGMAN_LOGO)

print(chosenWord)
# print(display)

win = True
guessHist = []

while('_' in display):


    print(HANGMANPICS[-totalLives])
    print(display)

    guess = input("Guess a letter: ").lower()

    clrscr()

    if guess in guessHist :
      print("You already guessed", guess)
      continue
    else :
      guessHist.append(guess)

    guessWin = False

    for i in range(len(chosenWord)) :
        if chosenWord[i] == guess :
            display[i] = guess

    if guess not in chosenWord:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        totalLives -= 1
        if (not totalLives):
            win = False
            break


if (win) :
    print("You guessed it right!")
    print("The word is",chosenWord)
    print("You Won!")
else :
    print("You Lose!")
