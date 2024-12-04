
class LimitedStack:
    def __init__(self, size):
        self.__stack = []
        self.__size = size
        self.foo = "UKAZKA"

    def push(self, item):
        if len(self.__stack) < self.__size:
            self.__stack.append(item)
            return True

        return False

    def pop(self):
        return self.__stack.pop()

    def top(self):
        return self.__stack[-1]

    def is_empty(self):
        return self.__stack == []

    def actual_size(self):
        return len(self.__stack)

    def max_size(self):
        return self.__size

    def __str__(self):
        return f"{self.__stack}"
        

        
# výsledky v main - volání z jiného souboru


