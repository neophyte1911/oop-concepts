'''
Class

A blueprint or template for creating objects. Think of it as a custom data type.

'''


class Person:
    """Represents a person with a name and age."""
    species = "Homo sapiens" # Class variable

    # Constructor
    def __init__(self, name, age):
        self.name = name  # Attributes
        self.age = age    # Attributes

    # Method
    def greet(self):
        return f"Hello, I’m {self.name} and I’m {self.age} years old."


'''
self ->
The first argument of every method is a reference to the current instance of
the class

In __init__, self refers to the object currently being created; so, in other class
methods, it refers to the instance whose method was called
'''



'''
Objects

A concrete instantiation of a class. Each object has its own state.
'''

alice = Person("Alice", 30) # Object // Instance of class person
bob   = Person("Bob", 25)

# accessing attributes:
print(alice.name)  # "Alice" // Instance variable
print(bob.age)     # 25
print(bob.species) # Class variable

print(Person.species)  # Class variable can be accessed via class


print(alice.species, bob.species)  # both "Homo sapiens"

Person.species = "H. sapiens" # Overriding class variable
print(alice.species, bob.species)  # both "H. sapiens"

alice.species = "Cyborg" # Overriding for single instance
print(alice.species)  # "Cyborg"
print(bob.species)    # still "H. sapiens"


''' 
Methods

A function defined inside a class that operates on instances.

'''

print(alice.greet())  # "Hello, I’m Alice and I’m 30 years old."
