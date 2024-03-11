from math import gcd

class Fraction(object):
    """
    A simple fraction class.
    """

    def __init__(self, numerator, denominator=1):
        """
        Creates a new fraction.
        """
        
        self.numerator = numerator
        self.denominator = denominator
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        
        
    def __str__(self):
        return('' + str(self.numerator) + '/' + str(self.denominator))

    def __add__(self, other):
        if self.denominator == other.denominator:
            self.numerator = self.numerator+other.numerator
            self.denominator = self.denominator
            return(Fraction(self.numerator, self.denominator))
        else:
            self.numerator = other.denominator*(self.numerator)+self.denominator *(other.numerator)
            self.denominator = self.denominator * other.denominator
            return(Fraction(self.numerator, self.denominator))
    def invert(self):
        return(Fraction(self.denominator,self.numerator))
    def float(self):
        return(self.numerator/self.denominator)
    def integer(self):
        return(int(self.numerator/self.denominator))
    def simplify(self):
        return(Fraction((self.numerator//gcd(self.numerator, self.denominator)),
                        (self.denominator//gcd(self.numerator, self.denominator))))

     def __add__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
        elif isinstance(other, int):
            new_numerator = self.numerator + other * self.denominator
            new_denominator = self.denominator
        else:
            return NotImplemented
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        if isinstance(other, Fraction):
            other = Fraction(-other.numerator, other.denominator)
            return self.__add__(other)
        elif isinstance(other, int):
            return self.__add__(-other)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        elif isinstance(other, int):
            return Fraction(self.numerator * other, self.denominator)
        else:
            return NotImplemented

    
    def __truediv__(self, other):
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ValueError("Cannot divide by zero fraction.")
            return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        elif isinstance(other, int):
            if other == 0:
                raise ValueError("Cannot divide by zero.")
            return Fraction(self.numerator, self.denominator * other)
        else:
            return NotImplemented

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

   

        
    

