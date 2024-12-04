"""
addLast (enqueue) – Vloží prvek do fronty.
deleteFirst (poll, dequeue) – Získá a odstraní první prvek (hlavu) fronty.
getFirst (peek) – Získá první prvek fronty.
isEmpty – Dotaz na prázdnost fronty.
size – Vrátí počet obsažených prvků.

"""

class Queue:
    def __init__(self):
        self.__queue = []

    def add_last(self, item):
        self.__queue.append(item)

    def delete_first(self):
        try:
            return self.__queue.pop(0)
        except:
            return None

    def get_peek(self):
        return self.__queue[0]

    def is_empty(self):
        return len(self.__queue) == 0

    def get_actual_size(self):
        return len(self.__queue)