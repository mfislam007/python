class Player:
    """Player-class: stores data on team colors and points."""
    teamcolor = "Blue"
    __points = 0

    def __init__(self):
       self.teamcolor = input("What color do I get?:")

    def tellscore(self):
        print("I am", self.teamcolor,", we have", self.__points, "points!")
    def goal(self):
        self.__points += 1


def main():
    player1 = Player()
    player2 = Player()
    player1.goal()
    player1.goal()
    player2.goal()
    player1.tellscore()
    player2.tellscore()

if __name__=="__main__":
    main()