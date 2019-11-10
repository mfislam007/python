class Player:
    teamcolor = "Blue"
    __points = 0

    def tellscore(self):
        print("I am", self.teamcolor, "we have", self.__points, "points!")
    def goal(self):
        self.__points += 1


def main():
    bigman = Player()
    bigman.goal()
    bigman.tellscore()

if __name__=="__main__":
    main()