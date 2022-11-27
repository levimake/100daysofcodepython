# 🚨 Don't change the code below 👇
two_digit_number = int(input("Type a two digit number: "))
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
sum = 0
while(two_digit_number):
    sum += two_digit_number % 10
    two_digit_number //= 10

print(sum)
