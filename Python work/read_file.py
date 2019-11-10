text = open("facts.txt","r")
content = text.readlines()
print("Following was read from the file:")
for i in content:
	print(i)
text.close()