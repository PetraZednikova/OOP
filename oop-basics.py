

class Human:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello wolrd, I am {self.name}")

        print("--------------------------")




l = list()
h1 = Human("John")
h2 = Human("Adam")
#h2.name = "Adam"

print(l)
print(h1)
print(h1.name)
print(h2.name)
h1.say_hello()

# task 2

class City:
    def __init__(self, city_name, region_name, country_name, num_citizens, zip_code, area_code):
        # Inicializace atributů třídy City
        self.city_name = city_name
        self.region_name = region_name
        self.country_name = country_name
        self.num_citizens = num_citizens
        self.zip_code = zip_code
        self.area_code = area_code

    # Metoda pro zobrazení všech dat o městě
    def display(self):
        print(f"City Name: {self.city_name}")
        print(f"Region Name: {self.region_name}")
        print(f"Country Name: {self.country_name}")
        print(f"Number of Citizens: {self.num_citizens}")
        print(f"ZIP Code: {self.zip_code}")
        print(f"Area Code: {self.area_code}")

    # Metody pro přístup k jednotlivým polím
    def get_city_name(self):
        return self.city_name

    def set_city_name(self, city_name):
        self.city_name = city_name

# Test třídy City
city = City("Praha", "Praha", "CZ", 12000, "12000", "9")
city.display()

# Změna názvu města a opětovné zobrazení
city.set_city_name("Ostrava")
print("\nUpdated City Name:")
city.display()


print("--------------------------")

#task 3
class Country:
    def __init__(self, country_name, continent, population, calling_code, capital, city_names):
        # Inicializace atributů třídy Country
        self.country_name = country_name
        self.continent = continent
        self.population = population
        self.calling_code = calling_code
        self.capital = capital
        self.city_names = city_names

    # Metoda pro zobrazení všech dat o zemi
    def display(self):
        print(f"Country Name: {self.country_name}")
        print(f"Continent: {self.continent}")
        print(f"Population: {self.population}")
        print(f"Calling Code: {self.calling_code}")
        print(f"Capital: {self.capital}")
        print(f"City Names: {', '.join(self.city_names)}")

    # Metody pro přístup k jednotlivým polím
    def get_country_name(self):
        return self.country_name

    def set_country_name(self, country_name):
        self.country_name = country_name

# Test třídy Country
country = Country("USA", "North America", 331000000, "+1", "Washington D.C.", ["New York", "Los Angeles", "Chicago"])
country.display()

# Změna hlavního města a opětovné zobrazení
country.capital = "New York"
print("\nUpdated Capital:")
country.display()


print("-----------------------")

#task 4

class Fraction:
    def __init__(self, numerator, denominator):
        # Inicializace čitatele a jmenovatele
        self.numerator = numerator
        self.denominator = denominator¨

    