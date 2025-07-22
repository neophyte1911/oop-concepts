class A:
    def method(self):
        print("A.method")

class B(A):
    def method(self):
        print("B.method")
        super().method()

class C(A):
    def method(self):
        print("C.method")
        super().method()

# D inherits from both B and C → diamond shape
class D(B, C):
    def method(self):
        print("D.method")
        super().method()

'''
    Single Inheritance: A child class inherits from a single parent class.
    B -> A, C -> A
    
    Multiple Inheritance: A child class inherits from more than one parent class.
    D -> B,C
    
    Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another class.
    D -> B -> A

    Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
    B -> A, C -> A

    Hybrid Inheritance: A combination of two or more types of inheritance.
    All above examples together form Hybrid inheritance
'''

'''

Method resolution order

Python uses the C3 linearization algorithm to produce a single, consistent lookup order.

MRO determines the order in which methods are resolved when multiple inheritance is involved.
Use the __mro__ attribute or mro() method to inspect the MRO of a class
'''

print(D.__mro__)

import inspect
print(inspect.getmro(D))
