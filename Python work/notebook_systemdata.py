import time

def readfile(name):
    try:
        readfile = open(name,'r')
        content = readfile.read()
        readfile.close()
        return content
    except IOError:
        return False
def addfile(name, uinput):
    try:
        uinput = uinput+":::"
        uinput += time.strftime("%X %x")
        addfile = open(name,'a')
        addfile.write(uinput+"\n")
        addfile.close()
    except IOError:
        return False
def emptyfile(name):
    try:
        emptyfile = open(name,'w')
        emptyfile.close()
    except IOError:
        return False

while True:
    selection=input('''(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit
Please select one: ''')
    if selection=='1':
        content=readfile("notebook.txt")
        print(content)
    if selection=='2':
        uinput=input("Write a new note: ")
        addfile("notebook.txt",uinput)
    if selection=='3':
        emptyfile("notebook.txt")
        print("Notes deleted.")
    if selection=='4':
        print("Notebook shutting down, thank you.")
        break