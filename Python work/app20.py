import pickle
import time

def readfile(filename):
    while True:
        try:
            readfile = open(filename,'rb')
            content = pickle.load(readfile)
            readfile.close()
            return content
        except IOError:
            newfile(filename)
            print("No default notebook was found, created one.")

def writefile(note, filename):
    try:
        writefile = open(filename, 'wb')
        pickle.dump(note, writefile)
        writefile.close()
    except IOError:
        return False

def newfile(filename):
    try:
        newfile = open(filename,'wb')
        note=[]
        pickle.dump(note, newfile)
        newfile.close()
    except IOError:
        return False

def editnote(note):
    print("The list has", len(note),"notes.")
    try:
        whichnote = int(input("Which of them will be changed?:"))
        print(note[whichnote])
        newnote = input("Give the new note: ")
        newnote = newnote+":::"
        newnote += time.strftime("%X %x")
        note[whichnote] = newnote
        return note
    except Exception:
        print("Incorrect value.")

def deletenote(note):
    print("The list has", len(note),"notes.")
    try:
        whichnote = int(input("Which of them will be deleted?:"))
        print("Deleted note", note[whichnote])
        note.pop(whichnote)
        return note
    except Exception:
        print("Incorrect value.")

def main():
    note = []
    filename = "notebook.dat"
    note = readfile(filename)
    while True:
        selection=input('''(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit
Please select one: ''')
        if selection == '1':
            for i in note:
                print(i)
        elif selection == '2':
            uinput=input("Write a new note: ")
            uinput = uinput+":::"
            uinput += time.strftime("%X %x")
            note.append(uinput)
        elif selection == '3':
            note = editnote(note)
        elif selection == '4':
            note = deletenote(note)
        elif selection == '5':
            writefile(note, filename)
            print("Notebook shutting down, thank you.")
            break

if __name__ == "__main__":
    main()