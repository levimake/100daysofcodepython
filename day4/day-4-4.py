import random

# Rock Paper Scissors ASCII Art
# Rock
choices = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",

# Paper
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",

# Scissors
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))
print(choices[user_choice])
print("Computer's Turn:")
pc_choice = random.randint(0,2)
print(choices[pc_choice])

message = "You Win!"

if user_choice == pc_choice :
    message = "Tie!"

else:
    if user_choice == 0 :
        if pc_choice == 1 :
            message = "Computer Win!"
    elif user_choice == 1 :
        if pc_choice == 2 :
            message = "Computer Win!"
    else :
        if pc_choice == 0 :
            message = "Computer Win!"

print(message)

