'''
dataclass module is introduced in Python 3.7 as a utility tool to make structured classes specially for storing data. These classes hold certain properties and functions to deal specifically with the data and its representation.

auto-generates __init__, __repr__, __eq__ and more:

'''

from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

p1 = Point(1, 2)
print(p1)              # Point(x=1, y=2)
print(p1 == Point(1,2))  # True


'''
Restrict dynamic attributes and save memory by pre-declaring allowed instance vars:
'''
class Node:
    __slots__ = ("value", "next")
    def __init__(self, value):
        self.value = value
        self.next = None
        self.other = 1 # AttributeError: 'Node' object has no attribute 'other'

n = Node(5)
