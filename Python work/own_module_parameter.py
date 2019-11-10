
def testme(string):
    if len(string) < 6:
        return False
    elif (len(string) >= 6) and (string.isalnum()) \
and not (string.isdigit()) and not (string.isalpha()):
        return True
    else:
        return False
