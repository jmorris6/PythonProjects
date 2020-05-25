# Create a program to find where to stand in Princess Eve's elimination game
# Every third person in line is eliminated. Find where to stand to always win
# when there are n participants

suitors = int(input("Enter the number of suitors: "))
suitorsLeft = []
for x in range(suitors):
    suitorsLeft.append(x+1)
position = 0
while len(suitorsLeft) > 1:
    position += 2
    position = position % len(suitorsLeft)
    print("Pop at: " + str(position))
    suitorsLeft.pop(position)
    print(suitorsLeft)
print(suitorsLeft)