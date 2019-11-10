text = input("Give a file name:")
readfile = open(text,"w")
print("Write something: ")
readfile.write(input())
readfile.close()
readfile = open(text,"r")
content = readfile.readlines()
for i in content:
    print("Wrote Attention", i, "to the file", text)
readfile.close()


