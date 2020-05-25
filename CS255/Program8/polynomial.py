class Polynomial():
    def __init__(self, coefficients = [], size = 0):
        self.size = size
        self.coefficients = coefficients

    def __mul__(self, other):
        "Return self*val"
        if isinstance(other, Polynomial):
            _s = self.coefficients
            _v = other.coefficients
            res = [0]*(len(_s)+len(_v)-1)
            for selfpow,selfco in enumerate(_s):
                for valpow,valco in enumerate(_v):
                    res[selfpow+valpow] += selfco*valco
        else:
            res = [co*other for co in self.coefficients]
        return self.__class__(res)
    def __str__(self):
        temp = ""
        for x in range(len(self.coefficients)):
            temp += str(self.coefficients[len(self.coefficients)-x-1])
            if (x != len(self.coefficients)-1  ):
                temp += "x^" + str(len(self.coefficients)-x-1) + " + "
        return temp
