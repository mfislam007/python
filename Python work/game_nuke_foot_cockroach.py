import random


def win():
    print("You WIN!")
    result = 1
    return result


def lose():
    print("You LOSE!")
    result = 3
    return result


def choiceDisplay(user, AI):
    print("You chose:", user)
    print("Computer chose:", AI)


def play(user):
    """ Takes user choice. Select AI's choice randomly. And decide who wins."""
    play = random.randint(1, 3)
    if play == 1:
        AI = "Foot"
    elif play == 2:
        AI = "Nuke"
    elif play == 3:
        AI = "Cockroach"

    if (AI == user) and (AI != "Nuke"):
        choiceDisplay(user, AI)
        print("it is a tie!")
        result = 2
        return result
    elif (AI == user) and (AI == "Nuke"):
        choiceDisplay(user, AI)
        print("Both LOSE!")
        result = 3
        return result
    elif user == "Foot":
        choiceDisplay(user, AI)
        if play == 2:
            return lose()
        elif play == 3:
            return win()
    elif user == "Nuke":
        choiceDisplay(user, AI)
        if play == 1:
            return win()
        elif play == 3:
            return lose()
    elif user == "Cockroach":
        choiceDisplay(user, AI)
        if play == 1:
            return lose()
        elif play == 2:
            return win()
    else:
        print("Incorrect selection.")
        return 4


def main():
    rounds = 0
    wonrounds = 0
    tierounds = 0
    while True:
        user = input("Foot, Nuke or Cockroach? (Quit ends):")
        if user == "Quit":
            print("You played", rounds, "rounds, and won", wonrounds, \
                  "rounds, playing tie in", tierounds, "rounds.")
            break
        else:
            result = play(user)
            if result == 1:  # When you win
                rounds += 1
                wonrounds += 1
            elif result == 2:  # When it's a tie
                rounds += 1
                tierounds += 1
            elif result == 3:  # When you lose
                rounds += 1


if __name__ == "__main__":
    main()