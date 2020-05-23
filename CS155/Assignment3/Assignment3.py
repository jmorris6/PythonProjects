#****************************************************************
#
#   CS155: Computer Science
#   Fall Semester, 2017
#   
#   Assignment #3: Averages
#   Recieve input from the user of three different numbers,
#   take these numbers and find the average between them
#
#   Programmed by: Jacob Morris
#
#**************************************************************** 

num1 = float(input("input your first number: "))
num2 = float(input("Input your second number: "))
num3 = float(input("Input your third number: "))
average = ((num1 + num2 + num3) / 3)
print("The average of the three input numbers is " + str(average))