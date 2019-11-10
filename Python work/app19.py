def readfile(name):
    readfile = open(name, 'r')
    content = readfile.read()
    readfile.close()
    return content


def addfile(name, uinput):
    addfile = open(name, 'a')
    content = addfile.write(uinput + "\n")
    addfile.close()
    return content


def emptyfile(name):
    emptyfile = open(name, 'w')
    content = emptyfile.close()

    return content


while True:
    selection = input('''(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit
Please select one: ''')
    if selection == '1':
        content = readfile("notebook.txt")
        print(content)
    if selection == '2':
        uinput = input("Write a new note: ")
        addfile("notebook.txt", uinput)
    if selection == '3':
        emptyfile("notebook.txt")
        print("Notes deleted.")
    if selection == '4':
        print("Notebook shutting down, thank you.")
        break