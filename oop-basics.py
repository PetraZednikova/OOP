

class Human:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello wolrd, Iam {self.name}")




l = list()
h1 = Human("John")
h2 = Human("Adam")
#h2.name = "Adam"

print(l)
print(h1)
print(h1.name)
print(h2.name)
h1.say_hello()
