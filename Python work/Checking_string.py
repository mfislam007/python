readfile = open("string.txt", "r")
content = readfile.readlines()
for str in content:
    if str.rstrip().isalnum():
        print(str, "was ok.")
    else:
        print(str, "was invalid")
readfile.close()