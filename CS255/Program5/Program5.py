# Create a class to implement fractions
# Allow for it to create decimal values and reducing the fractions

class Fraction():
    def __init__(self, num = 1, den = 1):
        self.numerator = num
        self.denominator = den

    def returnDecmial(self):
        return self.numerator / self.denominator


    def reduceFraction(self):
        x = self.numerator
        y = self.denominator
        while(y):
            x, y = y, x % y
        self.numerator /= x
        self.denominator /= x

    def printFraction(self):
        print(str(int(self.numerator)) + "/" + str(int(self.denominator)))

    def __add__(self, fraction2):
        f1 = self
        f2 = fraction2
        temp = f1.denominator
        f1.numerator *= f2.denominator
        f1.denominator *= f2.denominator

        f2.numerator *= temp
        f2.denominator *= temp

        tempFrac = Fraction(f1.numerator + f2.numerator, f1.denominator)
        tempFrac.reduceFraction()
        return tempFrac

    def __sub__(self, fraction2):
        f1 = self
        f2 = fraction2
        temp = f1.denominator
        f1.numerator *= f2.denominator
        f1.denominator *= f2.denominator

        f2.numerator *= temp
        f2.denominator *= temp

        tempFrac = Fraction(f1.numerator - f2.numerator, f1.denominator)
        tempFrac.reduceFraction()
        return tempFrac

    def __mul__(self, fraction2):
        temp = Fraction(self.numerator*fraction2.numerator, self.denominator*fraction2.denominator)
        temp.reduceFraction()
        return temp

    def reciprocal(self):
        temp = Fraction(self.denominator, self.numerator)
        temp.reduceFraction()
        return temp
    def __truediv__(self, fraction2):
        return (self * fraction2.reciprocal())

    def __neg__(self):
        temp = Fraction(-self.numerator, self.denominator)
        temp.reduceFraction
        return temp
numerator1 = int(input("Enter the first numerator: "))
denominator1 = int(input("Enter the first denominator: "))
numerator2 = int(input("Enter the second numerator: "))
denominator2 = int(input("Enter the second denominator: "))
fraction1 = Fraction(numerator1, denominator1)
fraction2 = Fraction(numerator2, denominator2)
quit = False
while quit != True:
    print("What would you like to do?")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Reciprocal of First Fraction")
    print("6. Negation of Second Fraction")
    process = int(input())
    if(process == 1):
        (fraction1 + fraction2).printFraction()
    elif(process == 2):
        (fraction1 - fraction2).printFraction()
    elif(process == 3):
        (fraction1 * fraction2).printFraction()
    elif(process == 4):
        (fraction1 / fraction2).printFraction()     
    elif(process == 5):
        (fraction1.reciprocal()).printFraction()  
    elif(process == 6):
        (-fraction2).printFraction()
    else:
        quit = True