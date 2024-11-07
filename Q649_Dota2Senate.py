# Question: Two parties - Radiant and Dire. Senate consists of senators from two parties. Senate decide on change in
# the game and voting is round-based. In each round, each senator can exercise one of two rights: Ban one senator's
# right: Senator can make another senator lose all his rights in this and all following rounds. Announce the victory:
# If this senator found senators who still have rights to vote are all from the same party, he can announce victory
# and decide on the change. Given string senate representing each senator's party belonging. Character R and D
# represent each party and if there are n senators, size of given string will be n. Round-based procedure starts from
# first senator to last senator in given order and will last until end of voting. All the senators who have lost
# their rights will be skipped during the procedure. Suppose every senator is smart enough and will play best
# strategy for his own party. Predict which party will finally announce victory and change the rules. Output should
# be name of party who won.


def predictPartyVictory(senate: str) -> str:
    rad = []
    dire = []
    for i in range(len(senate)):
        if senate[i] == "R":
            rad.append(i)
        else:
            dire.append(i)

    while rad and dire:
        r_index = rad.pop(0)
        d_index = dire.pop(0)
        if r_index < d_index:
            rad.append(r_index + len(senate))
        else:
            dire.append(d_index + len(senate))

    return "Radiant" if rad else "Dire"


def main():
    print(predictPartyVictory("RD"))
    print(predictPartyVictory("RDD"))


if __name__ == '__main__':
    main()
