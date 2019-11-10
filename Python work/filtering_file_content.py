readfile = open("strings.txt", "r")
content = readfile.readlines()
for str in content:
    if str.rstrip().isalnum():
        print(str.rstrip(), "was ok.")
    else:
        print(str.rstrip(), "was invalid")
readfile.close()