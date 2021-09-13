import math

class Poly:

    def __init__(self,poly):
        self.poly = poly

    def calcY(self, x):
        poly = self.poly
        y = 0
        for i in poly:
            y += i[0]*(x**i[1])
        return y

    def diff(self, order):
        poly = self.poly
        dPoly = [] #differentiated version of polynomial
        for n in range(order):
            for i in poly:
                dPoly.append([i[0]*i[1],i[1]-1])
            dPoly.pop(len(dPoly)-1)
            self.poly = dPoly

    def defInterg(self, lower, upper):
        poly = self.poly
        sPoly = [] #intergrated version of polynomial
        for i in poly:
            sPoly.append([i[0]/(i[1]+1),i[1]+1])
        upperInterg = Poly(sPoly).calcY(upper)
        lowerInterg = Poly(sPoly).calcY(lower)
        return (upperInterg-lowerInterg)



