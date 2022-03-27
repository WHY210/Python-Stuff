userinput = str(input("Enter Your birthday in the form of YYYY MM DAY."))

digit = 0
for number in userinput:
    if number not in "0123456789":
        continue
    else:
        digit += int(number)
    
newdigit = 0
for digit_numeber in str(digit):
    newdigit += int(digit_numeber)

print(newdigit)


    