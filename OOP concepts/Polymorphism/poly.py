'''
Polymorphism is all about flexible, extensible code—calling the same operation on different types without caring exactly which type it is.


Polymorphism allows methods to have the same name but behave differently based on the object's context. It can be achieved through method overriding or overloading.

Subtype polymorphism (inheritance/overriding)
Duck typing (any object with the right methods)
Operator overloading (magic methods like __add__, __len__, etc.)



1. Run-Time Polymorphism:
    (Subtype polymorphism)
    Demonstrated using method overriding in the Dog class and its subclasses (Labrador and Beagle).
    The correct sound method is invoked at runtime based on the actual type of the object in the list.

2. Compile-Time Polymorphism:

    Python does not natively support method overloading. Instead, we use a single method (add) with default arguments to handle varying numbers of parameters.
    Different behaviors (adding two or three numbers) are achieved based on how the method is called.

'''


# Subtype Polymorphism
# A base class defines a method signature; each subclass provides its own implementation.

class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement speak()")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def make_it_speak(animal: Animal):
    # We can call speak() on any Animal subtype
    print(animal.speak())

# Usage
make_it_speak(Dog())  # Woof!
make_it_speak(Cat())  # Meow!




# Duck typing (any object with the right methods)
# No formal base class needed—as long as an object has the expected method or attribute, it “fits”

class Duck:
    def quack(self):    print("Quack!")
    def swim(self):     print("Splash")

class Person:
    def quack(self):    print("I can quack, too!")
    def swim(self):     print("I can swim")

def in_pond(thing):
    thing.quack()  
    thing.swim()

in_pond(Duck())    # Quack! Splash
in_pond(Person())  # I can quack, too! I can swim


# Operator Overloading
# You define or reuse magic methods so built‑ins like +, len(), or indexing work across types.


class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        # vector + vector → new vector
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)   # Vector(4, 6)




# Inheritance Class Polymorphism
# Inheritance-based polymorphism occurs when a subclass overrides a method from its parent class, providing a specific implementation. This process of re-implementing a method in the child class is known as Method Overriding.  

class Animal:
    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"