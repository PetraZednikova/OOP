#stack = zásobník

""" Abstraktní datový typ zásobník specifikuje tyto operace:

push - vloží prvek na vrch zásobníku
pop - odstraní vrchol zásobníku
top - dotaz na vrchol zásobníku
isEmpty - dotaz na prázdnost zásobníku (size - dotaz na velikost zásobníku) """

"""
push - vloží prvek na vrch zásobníku
pop - odstraní vrchol zásobníku
top - dotaz na vrchol zásobníku
isEmpty - dotaz na prázdnost zásobníku (size - dotaz na velikost zásobníku)
"""

class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        return self.__stack.pop()

    def top(self):
        return self.__stack[-1]

    def is_empty(self):
        return self.__stack == []

    def actual_size(self):
        return len(self.__stack)

    def __str__(self):
        return f"{self.__stack}"