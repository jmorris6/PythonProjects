def fillMatrix(matrix):
    with open("p8in.txt", "r") as fileMatrix:
        dimensions = fileMatrix.readline().split()
        row = int(dimensions[0])
        for x in range(row):
            rowNums = fileMatrix.readline().split()
            matrix.insert(x, rowNums)
        matrix = matrix[:-1 :]
        return matrix, row

def rowMajor(matrix, row):
    for x in range(row):
        for y in range(int(len(matrix[x]))):
            print(matrix[x][y], end=" ")
        print("")

def columnMajor(matrix, row):
    column = int(len(matrix[0]))
    for x in range(column):
        for y in range(row):
            print(matrix[y][x], end=" ")
        print("")

def columnSums(matrix, row):
    column = int(len(matrix[0]))
    for x in range(column):
        sum = 0
        for y in range(row):
            sum += int(matrix[y][x])
        print(str(sum))

def rowProduct(matrix, row):
    for x in range(row):
        product = 1
        for y in range(int(len(matrix[x]))):
            product *= int(matrix[x][y])
        print(product)

def menu():
    matrix = [[]]
    matrix, row = fillMatrix(matrix)
    while True:
        print("What would you like to do?")
        print("1. Fill the matrix")
        print("2. Print in row-major")
        print("3. Print in column-major")
        print("4. Print Column Sums")
        print("5. Print Row Products")
        print("0. Quit")
        choice = int(input())
        if(choice == 1):
            matrix, row = fillMatrix(matrix)
        elif(choice == 2):
            rowMajor(matrix, row)
        elif(choice == 3):
            columnMajor(matrix, row)
        elif(choice == 4):
            columnSums(matrix, row)
        elif(choice == 5):
            rowProduct(matrix, row)
        else:
            break

menu()