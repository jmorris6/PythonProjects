#****************************************************************
#
#   CS155: Computer Science
#   Fall Semester, 2017
#   
#   Assignment #1: Bjarne's Game Store
#   Produce a simple billing invoice, using data obtained
#   from the keyboard user; output is directed to a disk file
#
#   Programmed by: Jacob Morris
#
#   Due Date: N/A
#**************************************************************** 

Report = open("Bjarnes_Invoice.txt", "w+")
answer = "Y"
while answer == "Y":
    Game = input("Enter name of the game: ")
    Quantity = input("How many do you want to buy? ")
    Cost = input("What's the unit cost? ")
    Total = int(Cost) * int(Quantity)
    Total = str(Total)
    Report.write("Game: " + Game+ " ")
    Report.write("Quantity: " + Quantity+ " ")
    Report.write("Cost: " + Cost+ " ")
    Report.write("Total: " + Total + " ")
    answer = input("Any more? (Y/N) ")
Report.close()
