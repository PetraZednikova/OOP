class Airplane:
    def __init__(self, airplane_type, max_passengers, current_passengers=0):
        # Inicializace atributů třídy
        self.airplane_type = airplane_type  # Typ letadla (např. Boeing 747)
        self.max_passengers = max_passengers  # Maximální počet pasažérů
        self.current_passengers = current_passengers  # Aktuální počet pasažérů v kabině

    # Přetížení operátoru == pro kontrolu, zda jsou typy letadel stejné
    def __eq__(self, other):
        return self.airplane_type == other.airplane_type

    # Přetížení operátorů + a - pro změnu počtu pasažérů
    def __add__(self, passengers):
        new_passengers = self.current_passengers + passengers
        if new_passengers > self.max_passengers:
            raise ValueError("Cannot exceed the maximum number of passengers!")
        return Airplane(self.airplane_type, self.max_passengers, new_passengers)

    def __sub__(self, passengers):
        new_passengers = self.current_passengers - passengers
        if new_passengers < 0:
            raise ValueError("Cannot have fewer than 0 passengers!")
        return Airplane(self.airplane_type, self.max_passengers, new_passengers)

    # Přetížení operátorů += a -= pro přímou změnu aktuálního počtu pasažérů
    def __iadd__(self, passengers):
        self.current_passengers += passengers
        if self.current_passengers > self.max_passengers:
            raise ValueError("Cannot exceed the maximum number of passengers!")
        return self

    def __isub__(self, passengers):
        self.current_passengers -= passengers
        if self.current_passengers < 0:
            raise ValueError("Cannot have fewer than 0 passengers!")
        return self

    # Přetížení operátorů >, <, >=, <= pro porovnání maximální kapacity letadel
    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    # Zobrazení informací o letadle
    def __str__(self):
        return (f"Airplane Type: {self.airplane_type}, "
                f"Max Passengers: {self.max_passengers}, "
                f"Current Passengers: {self.current_passengers}")

# Vytvoření dvou letadel
plane1 = Airplane("Boeing 747", 400, 100)
plane2 = Airplane("Airbus A380", 850, 200)

# Kontrola shody typů letadel
print(plane1 == plane2)  # False, typy jsou odlišné

# Zvýšení a snížení počtu pasažérů pomocí + a -
plane1 += 50
print(plane1)  # Aktuální pasažéři: 150

plane1 -= 20
print(plane1)  # Aktuální pasažéři: 130

# Přetížení + a - vytváří nové instance
new_plane = plane1 + 100
print(new_plane)  # Aktuální pasažéři: 230

# Porovnání maximální kapacity letadel
print(plane1 > plane2)  # False, protože 400 < 850
print(plane1 <= plane2)  # True, protože 400 <= 850