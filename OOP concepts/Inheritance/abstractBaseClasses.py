'''
Abstract Base Classes (ABCs) are used to define abstract
methods that must be implemented by subclasses. They
provide a way to enforce certain methods in subclasses.

Use the abc module to create ABCs and define abstract
methods using the @abstractmethod decorator.

'''


from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        """Produce the animal’s vocalization."""
        pass

    @abstractmethod
    def move(self):
        """Describe how the animal moves."""
        pass

# Valid subclass: implements both abstract methods
class Dog(Animal):
    def speak(self):
        return "Woof!"
    def move(self):
        return "Runs on 4 legs"

# Missing one or both methods → cannot instantiate
class Snake(Animal):
    def speak(self):
        return "Hiss"
    # def move(self): ...



dog = Dog()
print(dog.speak(), dog.move())
# >> Woof! Runs on 4 legs

snake = Snake()
# TypeError: Can't instantiate abstract class Snake with abstract methods move
