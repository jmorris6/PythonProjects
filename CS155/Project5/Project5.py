def completionPercentage(attempts, completions):
    if(attempts == 0):
        return 0
    else:
        return float(completions) / attempts
    
def rating(attempts, completions, yards, touchdowns, interceptions):
    if(attempts == 0):
        return 0
    else:
        rating = (3*completions)+yards+(10*touchdowns)
        rating /= (attempts + (8*interceptions))
        return rating
print("  Quarterback\t\tAtt.\tComp.\tPct.\tYards\tTD\tInt.\tRating")
print("---------------\t\t----\t-----\t----\t-----\t----\t----\t------")
players = open("project5.txt", "r+")
EndOfFile = False
bestRating = 0
bestPlayer = ""
loops = 0
while EndOfFile == False:
    playername = players.readline()
    if(playername == ""):
        EndOfFile = True
    else:
        playername = playername[:-1]
        attributes = players.readline().split()
        attempts = int(attributes[0])
        completions = int(attributes[1])
        yards = int(attributes[2])
        touchdowns = int(attributes[3])
        interceptions = int(attributes[4])
        compPercent = completionPercentage(attempts, completions)
        playerRating = rating(attempts, completions, yards, touchdowns, interceptions)
        print(playername + "\t\t" + str(attempts) + "\t" + str(completions) + "\t" + str(round(compPercent, 2)) + "\t" + str(yards) + "\t" + str(touchdowns) + "\t" + str(interceptions) + "\t" + str(round(playerRating, 2)))
        loops += 1
        if(bestRating < playerRating):
            bestRating = playerRating
            bestPlayer = playername
print("\nNumber of quarterbacks: " + str(loops))
print("\nBest rating: " + bestPlayer + " with rating of " + str(round(bestRating, 2)))
players.close()

