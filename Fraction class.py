class Fraction:
    def __init__(self,numerator ,denominator):
        self.num = numerator
        self.den = denominator

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self,other):
        temp_num = self.num * other.den + other.num * self.den
        temp_den = self.den * other.den
        return f"{temp_num}/{temp_den}"
    
    def __sub__(self,other):
        temp_num = self.num * other.den - other.num * self.den
        temp_den = self.den * other.den
        return f"{temp_num}/{temp_den}"
    
    def __mul__(self,other):
        temp_num = self.num * other.num
        temp_den = self.den * other.den
        return f"{temp_num}/{temp_den}"
    
    def __truediv__(self,other):
        temp_num = self.num * other.den
        temp_den = self.den * other.num
        return f"{temp_num}/{temp_den}"
