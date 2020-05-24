#****************************************************************
#
#   CS155: Computer Science
#   Fall Semester, 2017
#   
#   Project #4: Vending Machine
#   Create a simple vending machine that only handles money
#   in multiples of 5
#
#   Programmed by: Jacob Morris
#
#**************************************************************** 
import time
def getItem(money, choice):
    if choice > money:
        return -1
    else:
        return money - choice

def getChange(money):
    quarters, dimes, nickels = 0, 0, 0
    quarters = money // 25
    money -= (quarters * 25)
    dimes = money // 10
    money -= (dimes * 10)
    nickels = money // 5
    print("Change is: ")
    print(str(quarters) + " quarters")
    print(str(dimes) + " dimes")
    print(str(nickels) + " nickels")

money = int(input("Enter your money (only in multiples of 5): "))
if(money % 5 != 0):
    print("Error: Not a multiple of 5")
elif ((money < 45) or (money > 100)):
    print("Error: Invalid amount entered")
else:
    while money >= 45:
        retry = True
        choice = 0
        while retry:
            retry = False
            print("45 M&Ms")
            print("50 Jerky")
            print("75 Gum")
            print("100 Water")
            choice = int(input("Select your item: "))
            if (choice == 45):
                money = getItem(money, choice)
            elif (choice == 50):
                money = getItem(money, choice)
            elif (choice == 75):
                money = getItem(money, choice)
            elif (choice == 100):
                money = getItem(money, choice)
            else:
                print("Invalid choice")
                retry = True
            if(money == -1):
                retry = True
        print("\nSuccessfully bought " + str(choice))
        getChange(money)


