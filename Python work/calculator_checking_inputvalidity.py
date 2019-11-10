import math


def getnum():
    while True:
        try:
            num = int(input("Give a number: "))
            return num
        except Exception:
            print("This input is invalid.")


def main():
    print("Calculator")
    num1 = getnum()
    num2 = getnum()
    num1 = int(num1)
    num2 = int(num2)
    while True:
        print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(number1/number2)\
\n(6)cos(number1/number2)\n(7)Change numbers\n(8)Quit")
        print("Current numbers:", num1, num2)
        op = input("Please select something (1-6):")
        if op == "1":
            result = num1 + num2
            print("The result is:", result)
        elif op == "2":
            result = num1 - num2
            print("The result is:", result)
        elif op == "3":
            result = num1 * num2
            print("The result is:", result)
        elif op == "4":
            result = num1 / num2
            print("The result is:", result)
        elif op == "5":
            result = math.sin(num1 / num2)
            print("The result is:", result)
        elif op == "6":
            result = math.cos(num1 / num2)
            print("The result is:", result)
        elif op == "7":
            num1 = getnum()
            num2 = getnum()
        elif op == "8":
            print("Thank you!")
            break
        else:
            print("Selection was not correct.")


if __name__ == "__main__":
    main()