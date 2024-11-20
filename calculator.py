class Calculator:
    ans = None

    @classmethod
    def plus(cls, a, b):
        cls.ans = a + b
        return cls.ans

    """@classmethod
    def __str__(cls):
        cls.ans = 9999
        return f"{cls.ans}" """

    @staticmethod
    def minus(a, b):
        return a - b

"""def plus(a, b):
    return a + b"""

c1 = Calculator()
c2 = Calculator()

#print(Calculator.plus(2, 6))

c1.plus(2, 4)

print(c2.ans)

print(c1)

print(c2.ans)