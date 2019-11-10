print("Calculator")
num1 = int(input("Give the first number: "))
num2 = int(input("Give the second number: "))
while True:
 print("(1) +")
 print("(2) -")
 print("(3) *")
 print("(4) /")
 print("(5) Change numbers")
 print("(6) Quit")
 print("Current numbers: ", num1, num2)
 ope = input("Please select something (1-6):")
 if ope == "1":
    print("The result is:", num1 + num2)
 elif ope == "2":
    print("The result is:", num1 - num2)

 elif ope == "3":
    print("The result is:", num1 * num2)

 elif ope == "4":
    print("The result is:", num1 / num2)

 elif ope == "5":
    num1 = int(input("Give the first number: "))
    num2 = int(input("Give the second number: "))
    "/n"

 elif ope == "6":
    break

 else:
     print("Selection was not correct.")

print("Thank you!")