num1 = int(input("Give a number: "))
num2 = int(input("Give another number: "))
mod1 = num1 % 2
mod2 = num2 % 2
if mod1 == 0 and mod2 == 0:
    print("Both numbers are even.")
elif mod1 == 1 and mod2 == 1:
    print("Both numbers are odd.")

else:
    print("One of the numbers is even.")