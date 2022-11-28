# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
wordList1 = list("TRUE")
wordList2 = list("LOVE")

num1 = len([value for value in list((name1+name2).upper()) if value in wordList1])
num2 = len([value for value in list((name1+name2).upper()) if value in wordList2])

score = int(str(num1) + str(num2))

if score < 10 or score > 90 :
        print(f"Your score is {score}, you go together like coke and mentos.")    
elif score >= 40 and score <= 50 :
        print(f"Your score is {score}, you are alright together.")
else :
        print(f"Your score is {score}.")

