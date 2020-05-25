import math
class Complex():
    def __init__(self, real=0, imaginary = 0):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        if((self.real == other.real) and (self.imaginary == other.imaginary)):
            return True
        else:
            return False

    def __add__(self, other):
        temp = Complex(self.real + other.real, self.imaginary + other.imaginary)
        return temp

    def __sub__(self, other):
        temp = Complex(self.real - other.real, self.imaginary - other.imaginary)
        return temp

    def __mul__(self, other):
        tempReal = (self.real*other.real - self.imaginary*other.imaginary)
        tempImaginary = (self.real*other.imaginary + self.imaginary*other.real)
        return Complex(tempReal, tempImaginary)

    def __str__(self):
        if (self.imaginary < 0):
            return "(" + str(self.real) + " - " + str(-self.imaginary) + "i" + ")"
        else:
            return "(" + str(self.real) + " + " + str(self.imaginary) + "i" + ")"
        
    def __truediv__(self, other):
        conjugate = other.conj()
        numerator = self * conjugate
        denominator = other * conjugate
        numerator.real /= denominator.real
        numerator.imaginary /= denominator.real
        print(str(numerator))
        print(str(denominator))
    def conj(self):
        return Complex(self.real, -self.imaginary)

    def abs(self):
        return math.sqrt(self.real**2 + self.imaginary**2)