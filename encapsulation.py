class Human:
    def __init__(self, name):
        self.__name = name
        self._age = 0
        self.__secret = "Secret"

    def get_name(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def get_secret(self):
        return self.__secret

    def set_secret(self, secret):
        self.__secret = secret

    def del_secret(self):
        print(self.__secret, " UMIERAM")

    secret = property(
        fget=get_secret,
        fset=set_secret,
        fdel=del_secret,
        doc="Secret UMIERAM"
    )


class Sailor(Human):
    def __init__(self, name, position):
        Human.__init__(self, name)
        self.position = position

    def __str__(self):
        return f"{self.get_name()} is at {self.position}, age: {self._age}"

    def get_position(self):
        return self.position


s1 = Sailor('<NAME>', 0)
s2 = Sailor('<NAME>', 1)
h1 = Human('<NAME>')
h2 = Human('<NAME>')

print(s1)

h1.name = "John"
print(h1.name)
print("AGE: ", h1._age)
#print(h1.__name)
print(h1.get_name())
#print(h2.name)

print(h1.secret)
h1.secret = "CHANGE"
print(h1.secret)
del h1.secret