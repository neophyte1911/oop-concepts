'''
Inheritance, also called generalization, allows us to capture a hierarchal relationship
between classes and objects. For instance, a ‘fruit’ is a generalization of ‘orange’.

It refers to defining a new class with little or no modification to an existing
class.

The new class is called derived (or child) class and the one from which it
inherits is called the base (or parent) class.
Derived class inherits features from the base class, adding new features to it.

This results into re-usability of code.

SIMPLY PUT
- Reuse common code
- Specialize behavior (override or extend)
- Model real‑world “is‑a” relationships
'''

class Person:
    """Base class as before."""
    species = "Homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def greet(self):
        return f"Hello, I’m {self.name} and I’m {self.age}."

# ——— Subclassing Person ———
class Employee(Person):
    """An Employee is a Person who works at a company."""
    def __init__(self, name, age, company, salary):
        # call the Person initializer
        super().__init__(name, age) # Invokes parent's constructor
        self.company = company
        self.salary  = salary

    # override greet to include company
    def greet(self):
        base = super().greet()   # “Hello, I'm X and I'm Y.”
        return f"{base} I work at {self.company}."

    # add new method
    def give_raise(self, amount):
        self.salary += amount
