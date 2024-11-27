"""
class Animal:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello I am {self.name}")
    
class Dog(Animal):
    def make_sound(self):
        print("Haf haf")

d1 = Dog("Baryk")
d1.say_hello()

class Bird(Animal):
    def make_sound(self):
        print("pip pip")
b1 = Bird("Cooco")
b1.say_hello()


#task 1

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return f"Ahoj jsem {self.name} a je mi {self.age} let."

class Builder(Human):
    def __init__(self, name, age, specialization):
        Human.__init__(self, name, age)
        self.specialization = specialization

    def work(self):
        return f"Jsem stavitel a specializuju se na {self.specialization}"

class Sailor(Human):
    def __init__(self, name, age, ship_name):
        Human.__init__(self, name, age)
        self.ship_name = ship_name

    def work(self):
        return f"Jsem námořník pracující na lodi {self.ship_name}"

class Pilot(Human):
    def __init__(self, name, age, airline):
        Human.__init__(self, name, age)
        self.airline = airline
    def work(self):
        return f"Jsem pilot letajici pro {self.airline}"

b1 = Builder(name="Jan", age=35, specialization="Stavby mostu")
s1 = Sailor(name="Tom", age=29, ship_name= "Aurora")
p1 = Pilot(name= "Raul", age=38, airline="Czech Airlines")


print(b1.introduce()) 
print(b1.work())      

print(s1.introduce())   
print(s1.work())        

print(p1.introduce())
print(p1.work()) 

print()

print()
"""

#task 2

class Passport:
    def __init__(self, name, surname, passport_number, country):
        self.name = name
        self.surname = surname
        self.passport_number = passport_number
        self.country = country

    def display_info(self):
        print(f"Name: {self.name}, Surname: {self.surname}, Passport Number: {self.passport_number}, Country: {self.country}") 


class ForeignPassport(Passport):
    def __init__(self, name, surname, passport_number, country, foreign_passport_number):
        """Inicializuje informace o zahraničním pasu."""
        super().__init__(name, surname, passport_number, country)  # Inicializace základních atributů
        self.foreign_passport_number = foreign_passport_number
        self.visas = []  # Seznam víz

    def add_visa(self, visa):
        """Přidá nové vízum do seznamu víz."""
        self.visas.append(visa)

    def display_foreign_info(self):
        """Zobrazí informace o zahraničním pasu a vízech."""
        visa_info = ", ".join(self.visas) if self.visas else "No visas"
        return (f"{self.display_info()}, Foreign Passport Number: {self.foreign_passport_number}, "
                f"Visas: {visa_info}")  
passport = Passport(name="John", surname="Doe", passport_number="123456", country="USA")
print(passport.display_info())  # "Name: John, Surname: Doe, Passport Number: 123456, Country: USA"

# Vytvoření zahraničního pasu
foreign_passport = ForeignPassport(name="Jane", surname="Smith", passport_number="654321", country="Canada", foreign_passport_number="987654")
foreign_passport.add_visa("Schengen")
foreign_passport.add_visa("UK")
print(foreign_passport.display_foreign_info())