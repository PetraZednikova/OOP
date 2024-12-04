

class LimitedQueue:
    def __init__(self, size):
        self.__queue = []
        self.__size = size

    def add_last(self, item):
        if len(self.__queue) < self.__size:
            self.__queue.append(item)
            return True

        return False

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

    def get_max_size(self):
        return self.__size