class Player:
    teamcolor = ""
    points = ""


def main():
    RM = Player()
    RM.teamcolor = "Blue"
    RM.points = "300"
    print("The", RM.teamcolor, "contender has", RM.points, "points!")


if __name__ == "__main__":
    main()
