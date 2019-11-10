words = open("words.txt","r")
container = words.readlines()
container.sort()
for i in container:
 print (i)
words.close()