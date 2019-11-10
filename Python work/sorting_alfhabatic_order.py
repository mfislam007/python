words = open("words.txt","r")
container = words.readlines()
container.sort()
print("Words in an alphabetical order:")
for i in container:
 print (i)
words.close()