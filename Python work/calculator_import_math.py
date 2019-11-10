import math

print("Calculator")
number1 = int(input("Give the first number: "))
number2 = int(input("Give the second number: "))
while True:
    print("(1) +")
    print("(2) -")
    print("(3) *")
    print("(4) /")
    print("(5) sin(number1/number2)")
    print("(6) cos(number1/number2)")
    print("(7) Change numbers")
    print("(8) Quit")
    print("Current numbers: ", number1, number2)
    ope = input("Please select something (1-6):")
    if ope == "1":
        print("The result is:", number1 + number2)
    elif ope == "2":
        print("The result is:", number1 - number2)

    elif ope == "3":
        print("The result is:", number1 * number2)

    elif ope == "4":
        print("The result is:", number1 / number2)

    elif ope == "5":
        print("The result is:", math.sin(number1 / number2))

    elif ope == "6":
        print("The result is:", math.cos(number1 / number2))

    elif ope == "7":
        number1 = int(input("Give the first number: "))
        number2 = int(input("Give the second number: "))
        "/n"

    elif ope == "8":
        break

    else:
        print("Selection was not correct.")

print("Thank you!")