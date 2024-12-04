"""1.	Abstraktná trieda View:
	•	Obsahuje:
	•	Atribúty: name (názov), position (pozícia ako tuple).
	•	Abstraktnu metódu move(new_position: tuple), ktorá nastaví novú pozíciu.

2.	Rozhranie Zobrazitelny:
	•	Obsahuje:
	•	Abstraktnu metódu show(), ktorá vypíše informácie o komponente.

3.	Triedy Button a TextLabel:
	•	Obe triedy dedia od View a implementujú Zobrazitelny.
	•	Implementácia:
	•	Button má navyše atribút label (text na tlačidle),
	    a funkciu ktoru spusta pod volanim metody click. # BONUS
	•	TextLabel má navyše atribút text (zobrazovaný text).
	•	Metóda show() vypíše konkrétne informácie o tlačidle alebo textovom štítku."""


from abc import ABC, abstractmethod


class View(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.position = position

    @abstractmethod
    def move(self, new_position: tuple):
        pass


