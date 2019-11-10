import random
Foot=1
Nuke=2
Cockroach=3
you = input("Foot, Nuke or Cockroach? (Quit ends):")
print("You chose:",you)
if you == "Foot":
  computer = random.randint("Nuke", "Cockroach")
  print("Computer chose:", computer)
elif you == "Nuke":
 computer = random.randint("Foot","Cockroach")
 print("Computer chose:", computer)
elif you == "Cockroach":
 computer = random.randint("Nuke", "Foot")
 print("Computer chose:", computer)
else:
 print("Incorrect selection.")



print("You LOSE!")
print("You WIN!")

print("You played",  "rounds, and won", "rounds, playing tie in", "rounds.")


