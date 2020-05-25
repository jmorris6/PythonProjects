def fillArrays():
    contestantID, completedRounds, totalScore = [],[],[]
    with open("turkeys.txt", "r") as table:
        contestant = table.readline().split()
        while (contestant != []):
            contestantID.append(contestant[0])
            completedRounds.append(contestant[1])
            totalScore.append(contestant[2])
            contestant = table.readline().split()
    return contestantID, completedRounds, totalScore

def displayTable(contestantID, completedRounds, totalScore):
    for x in range(len(contestantID)):
        if(int(completedRounds[x]) == 0):
            average = 0
        else:
            average = int(totalScore[x]) / int(completedRounds[x])
        print(contestantID[x] + "\t" + completedRounds[x] + "\t" + totalScore[x] + "\t" + str(average))

def addScore(ID, contestantID, completedRounds, totalScore):
    position = -1
    for x in range(len(contestantID)):
        if(ID == int(contestantID[x])):
            position = x
    if (position == -1):
        print("Invalid user ID")
    else:
        print(completedRounds[position])
        if(int(completedRounds[position]) == 3):
            print("Contestant has already completed all three rounds")
        else:
            score = int(input("Enter the score for the new round: "))
            while (score > 25) or (score < 0):
                print("Invalid score input")
                score = int(input("Enter the score for the new round: "))
            temp = int(completedRounds[position]) + 1
            completedRounds[position] = str(temp)
            temp = int(totalScore[position]) + score
            totalScore[position] = str(temp)

def save(contestantID, completedRounds, totalScore):
    with open("turkeys.txt", "w") as table:
        for x in range(len(contestantID)):
            table.write(contestantID[x] + " " + completedRounds[x] + " " + totalScore[x] + "\n")

contestantID, completedRounds, totalScore = fillArrays()
displayTable(contestantID, completedRounds, totalScore)
userInput = -2
while userInput != -1:
    print("What would you like to do?")
    print("0. Display Table")
    print("-1. End the program")
    print("ID. Update a contestants score")
    userInput = int(input())
    if(userInput == 0):
        displayTable(contestantID, completedRounds, totalScore)
    elif(userInput == -1):
        save(contestantID, completedRounds, totalScore)
    else:
        addScore(userInput, contestantID, completedRounds, totalScore)


