def readfile():
 myfile = open("number.txt","r")
 myfile = (myfile)
 content = myfile.readlines()
 for i in content:
  myfile.close()
 return i

def main():
 file = input("Give the file name:")
 try:
  file == "number.txt"
  print("The result was", readfile())
 except(TypeError):
     print("no file")
 except(IOError):
     print("no content")



if __name__ == "__main__":
    main()