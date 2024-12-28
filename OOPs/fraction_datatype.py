class Fraction:
    def __init__(self,n,d):
        self.num = n
        self.den = d

    # This is also special method / constructor / ductor method is called automatically 
    # whenever we print that object in print method 

    def __str__(self):
        return f'{self.num}/{self.den}'


    # This is one of special method / constructor / ductor method is called automatically
    # whenever we want addition of two object in print()

    def __add__(self,other):
        if self.den == other.den :
            numerator = self.num + other.num
            denominator = self.den
            return f'{numerator}/{denominator}'
        else:
            numerator = self.num * other.den + self.den * other.num
            denominator = self.den * other.den
            return f'{numerator}/{denominator}'

    # This is one of special method / constructor / ductor method is called automatically
    # whenever we want substraction of two object in print()

    def __sub__(self,other):
        if self.den == other.den :
            numerator = self.num - other.num
            denominator = self.den
            return f'{numerator}/{denominator}'
        else:
            numerator = self.num * other.den - self.den * other.num
            denominator = self.den * other.den
            return f'{numerator}/{denominator}'
    
    # This is one of special method / constructor / ductor method is called automatically
    # whenever we want multiplication of two object in print()

    def __mul__(self,other):
        numerator = self.num * other.num
        denominator = self.den * other.den
        return f'{numerator}/{denominator}'
    

    def __truediv__(self,other):
        numerator = self.num * other.den
        denominator = self.den * other.num
        return f'{numerator}/{denominator}'
