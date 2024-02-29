firstNum = 0
secondNum = 0
operator = ""

firstNum = float(input("Write number "))
secondNum = float(input("Write number "))
operator = input("write your operator")

if operator == "+":
    print(str(firstNum + secondNum))
elif operator == "-":
    print(str(firstNum - secondNum))
elif operator == "/":
    if secondNum != 0:
    print(str(firstNum / secondNum))
    else:
    print("The second number cannot be 0")
else:
    print(Error)

# % moduLo
#    11 % 2 = 1

# Take 2 numbers from the user, and print if the 1st number can be evenly divided by the second number
    