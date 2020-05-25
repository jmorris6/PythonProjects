# Create a class to implement fractions
# Allow for it to create decimal values and reducing the fractions

class Fraction():
    def __init__(self, num, den):
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

firstFraction = Fraction(30, 45)
firstFraction.printFraction()
print(str(round(firstFraction.returnDecmial(), 3)))
secondFraction = Fraction(50, 100)
secondFraction.reduceFraction()
secondFraction.printFraction()