# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0
#size
bill += 15 if size == "S" else 20 if size == "M" else 25 if size == "L" else None
#pepperoni
if add_pepperoni == "Y" :
        bill += 2 if size == "S" else 3 if size in ["M","L"] else None
        #extra_cheese
        bill += 1 if extra_cheese == "Y" else 0

print(f"Your final bill is: ${bill}.")
