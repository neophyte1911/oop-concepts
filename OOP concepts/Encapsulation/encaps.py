'''

Encapsulation is the bundling of data (attributes) and methods (functions) within a class, restricting access to some components to control interactions.


    Protects data from unauthorized access and accidental modification.
    Controls data updates using getter/setter methods with validation.
    Enhances modularity by hiding internal implementation details.
    Simplifies maintenance through centralized data handling logic.
    Reflects real-world scenarios like restricting direct access to a bank account balance.

Types of Encapsulation:

    Public Members: Accessible from anywhere.
    Protected Members: Accessible within the class and its subclasses.
    Private Members: Accessible only within the class.

    Public Members: Easily accessible, such as name.
    Protected Members: Used with a single _, such as _breed. Access is discouraged but allowed in subclasses.
    Private Members: Used with __, such as __age. Access requires getter and setter methods.
'''

class Dog:
    def __init__(self, name, breed, age):
        self.name = name  # Public attribute
        self._breed = breed  # Protected attribute
        self.__age = age  # Private attribute

    # Public method
    def get_info(self):
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"

    # Getter and Setter for private attribute
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")

# Example Usage
dog = Dog("Buddy", "Labrador", 3)

# Accessing public member
print(dog.name)  # Accessible

# Accessing protected member
print(dog._breed)  # Accessible but discouraged outside the class

#print(dog.age) # raises error
# Accessing private member using getter
print(dog.get_age())

# Modifying private member using setter
dog.set_age(5)
print(dog.get_info())



'''

Encapsulation works at method level as well

'''


class Example:
    def public_method(self):
        """Any code can call me."""
        print("Public")

    def _protected_method(self):
        """By convention, ‘protected’—discouraged for outsiders, but still accessible."""
        print("Protected")

    def __private_method(self):
        """Truly private via name-mangling—only accessible inside the class."""
        print("Private")

    def run_all(self):
        # Inside the class you can call your ‘private’ method:
        self.__private_method()
        self._protected_method()
        self.public_method()



e = Example()
e.public_method()       # ✅ works
e._protected_method()   # ⚠️ works, but “you shouldn’t” from outside
e.__private_method()    # ❌ AttributeError!
