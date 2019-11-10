import time


def readfile(name):
    while True:
        try:
            readfile = open(name, 'r')
            content = readfile.read()
            readfile.close()
            return content
        except IOError:
            emptyfile(name)
            if name == "notebook.txt":
                print("No default notebook was found, created one.")
            else:
                print("No notebook with that name detected, created one.")


def writefile(name, uinput):
    try:
        uinput = uinput + ":::"
        uinput += time.strftime("%X %x")
        addfile = open(name, 'a')
        addfile.write(uinput + "\n")
        addfile.close()
    except IOError:
        return False


def emptyfile(name):
    try:
        emptyfile = open(name, 'w')
        emptyfile.close()
    except IOError:
        return False


def main():
    filename = "notebook.txt"
    readfile(filename)
    while True:
        print("Now using file", filename)
        selection = input('''(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Change the notebook
(5) Quit
Please select one: ''')
        if selection == '1':
            content = readfile(filename)
            print(content)
        elif selection == '2':
            uinput = input("Write a new note: ")
            writefile(filename, uinput)
        elif selection == '3':
            emptyfile(filename)
            print("Notes deleted.")
        elif selection == '4':
            filename = input("Give the name of the new file: ")
            readfile(filename)
        elif selection == '5':
            print("Notebook shutting down, thank you.")
            break


if __name__ == "__main__":
    main()