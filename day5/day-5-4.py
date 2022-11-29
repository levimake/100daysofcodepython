#Write your code below this row 👇

for i in range(1,101) :
    if i % 3 == 0 :
        message = "Fizz"
        if i % 5 == 0 :
            message += "Buzz"
    elif i % 5 == 0 :
        message = "Buzz"
    else :
        message = str(i)
    print(message)
