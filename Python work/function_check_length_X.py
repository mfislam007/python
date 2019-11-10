def tester(givenstring ="Too short"):
    print(givenstring)
while True:
    word = input("Write something (quit ends):")
    if word == "quit":
        break
    else:
     if len(word) < 10:
        tester()
     else:
        if "X" in word:
            print(word)
            print("X spotted")
        else:
            print(word)


