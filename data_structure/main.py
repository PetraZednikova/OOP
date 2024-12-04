from stack import Stack
from limited_stack import LimitedStack

"""-> datova struktura
-> zlozitost
-> asymptoticka zlozitost
-> amortizovna zlozitost
-> najhorsi pripad


adresa + index * velkost pametovej bunky

class Node:
    def __init__(self, value):
        self.value = value
        self.neighboors = [( 2 ,n1), n2, n3]


n4.neighboors = [n3]
n3.neighboors = [( 2 ,n1), n2]"""

"""
s = Stack()
print(s.__stack)
print(s.is_empty())
print(s)

s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.is_empty())
print(s)
print(s.pop())
print(s.pop())
print(s.pop())
print(s)"""


s = LimitedStack(3)
#print(s.foo)
#print(s.__stack)
print(s.is_empty())
print(s)

print(s.push(1))
print(s.push(2))
print(s.push(3))
print(s.push(4))
print(s.is_empty())
print(s)
print(s.pop())
print(s.pop())
print(s.pop())
print(s)
