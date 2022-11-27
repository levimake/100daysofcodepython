# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
yearsLeft = 90 - int(age)
daysLeft = yearsLeft * 365
weeksLeft = yearsLeft * 52
monthsLeft = yearsLeft * 12

print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.")
