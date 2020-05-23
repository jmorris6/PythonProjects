#****************************************************************
#
#   CS155: Computer Science
#   Fall Semester, 2017
#   
#   Project #1: Una's Interiors
#   Produce a simple program to estimate the cost of painting
#   projects
#
#   Programmed by: Jacob Morris
#
#**************************************************************** 
import math
room = input("Describe room: ")
length, width = input("Enter room length and width (in feet) separated by a space: ").split()
length = float(length)
width = float(width)
price = float(input("What is the price of a gallon of paint? "))
area = (2*length*8)+(2*width*8) + (length*width)
print("Room description: " + room)
print("Total area: " + str(area) + " square feet")
requiredGallons = area / 350
requiredGallons = math.ceil(requiredGallons)
print("Number of gallons: " + str(requiredGallons))
print("Total cost: $" + str(requiredGallons*price))