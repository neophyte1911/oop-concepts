'''

SOLID is a set of design principles that promote good software
design and maintainability.

Single Responsibility Principle (SRP): A class
should have only one reason to change.

Open/Closed Principle (OCP): Software entities
should be open for extension but closed for
modification.

Liskov Substitution Principle (LSP): Subtypes
must be substitutable for their base types.

Interface Segregation Principle (ISP): Clients
should not be forced to depend on interfaces they
do not use.

Dependency Inversion Principle (DIP): High-level
modules should not depend on low-level modules;
both should depend on abstractions

'''

from abc import ABC, abstractmethod

# 1. Single Responsibility Principle (SRP)
#  every class should have a single responsibility or single job or single purpose
# ————————————————————————————————————————————————
# Bad: one class manages both user data and persistence
class UserManagerBad:
    def __init__(self, name): self.name = name
    def save(self):
        with open("users.txt", "a") as f:
            f.write(self.name + "\n")
    def send_welcome_email(self):
        # … email logic …
        pass

# Good: split responsibilities
class User:
    def __init__(self, name): self.name = name

class UserRepository:
    def save(self, user: User):
        with open("users.txt", "a") as f:
            f.write(user.name + "\n")

class EmailService:
    def send_welcome(self, user: User):
        # … email logic …
        pass


# 2. Open/Closed Principle (OCP)
# you should be able to extend a class behavior, without modifying it. 
# ————————————————————————————————————————————————
# Open for extension, closed for modification
class Discount:
    def apply(self, amount): return amount

# New behavior added via subclass—no edit to Discount
class SeasonalDiscount(Discount):
    def apply(self, amount): return amount * 0.9

def checkout(amount, discount: Discount):
    return discount.apply(amount)


# 3. Liskov Substitution Principle (LSP)
# This principle ensures that any class that is the child of a parent class should be usable in place of its parent without any unexpected behaviour. 
# ————————————————————————————————————————————————
# Subclasses must honor parent’s contract
class Rectangle:
    def __init__(self, w, h): self._w, self._h = w, h
    def area(self): return self._w * self._h

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    # area() still works—no surprises

def print_area(rect: Rectangle):
    print(rect.area())

print_area(Rectangle(2, 3))  # 6
print_area(Square(4))        # 16


# 4. Interface Segregation Principle (ISP)
#  avoiding fat interface and give preference to many small client-specific interfaces
# ————————————————————————————————————————————————
# Break “fat” interfaces into focused ones
class Reader(ABC):
    @abstractmethod
    def read(self): ...

class Writer(ABC):
    @abstractmethod
    def write(self, data): ...

class FileHandler(Reader, Writer):
    def __init__(self, path): self.path = path
    def read(self): ...
    def write(self, data): ...

'''
A ReadOnlyCache that only needs to fetch data, you can just subclass Reader—and you’re not dragged into providing a no‑op write() method you’ll never use.
'''

# 5. Dependency Inversion Principle (DIP)
# High-level modules should not depend on low-level modules. Both should depend on abstractions
# ————————————————————————————————————————————————
# High‑level code depends on abstraction, not concretion
class Logger(ABC):
    @abstractmethod
    def log(self, msg): ...

class ConsoleLogger(Logger):
    def log(self, msg): print(msg)

class App:
    def __init__(self, logger: Logger):
        self._logger = logger
    def run(self):
        self._logger.log("App started")

# wiring
app = App(ConsoleLogger())
app.run()


'''

SOLID principles make code easier to maintain. When each class has a clear responsibility, it's simpler to find where to make changes without affecting unrelated parts of the code.
These principles support growth in software. For example, the Open/Closed Principle allows developers to add new features without changing existing code, making it easier to adapt to new requirements.
SOLID encourages flexibility. By depending on abstractions rather than specific implementations (as in the Dependency Inversion Principle), developers can change components without disrupting the entire system


'''