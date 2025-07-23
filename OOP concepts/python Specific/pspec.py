from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

p1 = Point(1, 2)
print(p1)              # Point(x=1, y=2)
print(p1 == Point(1,2))  # True
