
def testme(string):
    if len(string) < 6:
        return False
    elif (len(string) >= 6) and (string.isalnum()) \
and not (string.isdigit()) and not (string.isalpha()):
        return True
    else:
        return False

def printme(string):
    print("I got: ", string)
    print("The parameter was", len(string), "characters long.")