# pres tuple, ak presahujem velikost prvek s najmensou prioritou zahodim aby som pridal
# vysiu prioritu, ak novy ma najnisiu tak ho nepridam



class LimitedPriorityQueue:
    def __init__(self, size):
        self.__queue = []
        self.__size = size

    def add_last(self, item, priority=1):
        for i, n in enumerate(self.__queue):
            if priority > n[0]:
                self.__queue.insert(i, (priority, item))
                break
        else:
            self.__queue.append((priority, item))

        if len(self.__queue) > self.__size:
            self.__queue.pop()


    def delete_first(self):
        try:
            return self.__queue.pop(0)[1]
        except:
            return None

    def get_peek(self):
        return self.__queue[0][1]

    def is_empty(self):
        return len(self.__queue) == 0

    def get_actual_size(self):
        return len(self.__queue)

    def get_max_size(self):
        return self.__size

    def __str__(self):
        """Zobrazí obsah fronty: priority a hodnoty."""
        return " -> ".join([f"[{priority}, {item}]" for priority, item in self.__queue])