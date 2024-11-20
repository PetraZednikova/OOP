class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __eq__(self, other):
        return self.denominator == other.denominator and self.numerator == other.numerator

    def __add__(self, other):
        pass

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"



l1 = [1]
l2 = [1]

f = Fraction(1, 2)
f2 = Fraction(1, 2)
f3 = f2

print(f)
print(f2)
print(f3)
print(l1)

print("provnanie1: ", f == f2)
print("provnanie2: ", f3 == f2)
print("provnanie3: ", f3.__eq__(f2))


print("list")
print(l1 == l2)


print(Fraction.mro())