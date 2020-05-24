#****************************************************************
#
#   CS155: Computer Science
#   Fall Semester, 2017
#   
#   Project #3: Leo's Computer Shop
#   Print an invoice for purchasing a computer
#
#   Programmed by: Jacob Morris
#
#**************************************************************** 
print("Leo's Computer Ordering System\n")
print("H. Home Model $399.00")
print("W. Work Model $599.00")
print("G. Gaming Model $749.00")
computerModel = input("Select (H, W, G)? ")
if((computerModel != "H") and (computerModel != "W") and (computerModel != "G")):
    print("Invalid choice (must be H,W,G)")
else:
    print("Your computer comes with 8GB of memory. You may upgrade if you wish")
    print("A 16GB upgrade costs $50.00 adn a 32GB upgrade costs $100.00")
    memoryUpgrade = int(input("Enter 0 to stay with 8GB, 1 for 16 GB, or 2 for 32 GB: "))
    printer = input("A printer costs $150.00. Would you like a printer (Y/N)? ")
    print("-----------INVOICE--------------")
    total = 0
    if(computerModel == "H"):
        print("Home Computer Model: 399.00")
        total += 399.00
    elif(computerModel == "W"):
        print("Work Computer Model: 599.00")
        total += 599.00
    else:
        print("Gaming Computer Model: 749.00")
        total += 749.00
    
    if (memoryUpgrade == 1):
        print("16 GB Memory Upgrade: 50.00")
        total += 50.00
    elif(memoryUpgrade == 2):
        print("32 GB Memory Upgrade: 100.00")
        total += 100.00
    
    if((printer == "Y") or (printer == "y")):
        print("Printer: 150.00")
        total += 150.00
    print("Total due: " + str(total))
    print("--------------------------------")