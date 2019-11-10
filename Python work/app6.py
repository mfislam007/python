text = "notebook.txt"
while True:
 print("(1) Read the notebook")
 print("(2) Add note")
 print("(3) Empty the notebook")
 print("(4) Quit")
 sel = input("Please select one:")
 if sel == "1":
  text = open ("notebook.txt","r")
  content = text.readlines()
  for i in content:
    print(i)
  text.close()
 elif sel == "2":
  text = open("notebook.txt", "w")
  content = text.write(input("Write a new note:"))
  for i in content:
      print(i)
  text.close()
  text = open ("notebook.txt","r")
  content2 = text.readlines()
  for k in content2:
   print(k)
  text.close()
 elif sel == "3":
  text = open("notebook.txt", "a")
  content3 = text.write("")
  for k in content3:
      print(k)
  text.close()
  text = open ("notebook.txt","r")
  content = text.readlines()
  for i in content:
   print(i)
  text.close()
 elif sel == "4":
  break
 else:
  print("error")
print("Notebook shutting down, thank you.")