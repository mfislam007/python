print("Calculator")
num1=int(input("Give the first number: "))
num2=int(input("Give the second number: "))
print("(1) +")
print("(2) -")
print("(3) *")
print("(4) /")
ope=input("Please select something (1-4):")
if ope == "1":
	print("The result is:", num1+num2)
elif ope == "2":
	print("The result is:", num1-num2)

elif ope == "3":
	print("The result is:", num1*num2)

elif ope == "4":
	print("The result is:", num1/num2)

else :
	print("Selection was not correct.")