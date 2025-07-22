class Person:
    """Represents a person with a name and age."""
    species = "Homo sapiens"  # Class variable

    def __init__(self, name, age):
        self.name = name      # Instance attribute
        self.age = age        # Instance attribute

    def greet(self):
        return f"Hello, I’m {self.name} and I’m {self.age} years old."



    # ——— Magic Methods ———

    '''
    
    REPRESENTATION
    
    '''

    def __repr__(self):
        # Unambiguous: how you’d recreate this object in code
        return f"Object => Person(name={self.name!r}, age={self.age}, species = {self.species})"
    #calling only object

    def __str__(self):
        # Readable: what print() and str() will show
        return f"{self.name} ({self.species}, {self.age} years old)"
    #Calling print(object)


    '''
    
    COMPARISON
    
    '''
    def __eq__(self, other):
        # Equality check: True if same type and same data
        if not isinstance(other, Person):
            return NotImplemented
        return (self.name, self.age) == (other.name, other.age)
    # ALSO __ne__ (not equal)

    def __lt__(self, other):
        # Allows sorting by age: p1 < p2
        if not isinstance(other, Person):
            return NotImplemented
        return self.age < other.age
    # Also __le__, __gt__, __ge__ for Comparison
    




    '''
    
    CONTEXT MANAGEMENT
    
    '''
    def __len__(self):
        # Allow len(person) → length of their name
        return len(self.name)

    # Make Person callable: calling returns their greeting
    def __call__(self):
        return self.greet()

    # Context manager: auto-print on enter/exit
    def __enter__(self):
        print(f"[Entering context for {self.name}]")
        return self

    def __exit__(self, exc_type, exc, tb):
        print(f"[Exiting context for {self.name}]")
        # don’t suppress exceptions: return False


    '''
    
    GETTERS and SETTERS
    
    we are requesting that the object change its sequence data, whereas directly setting instance variables just reaches in and changes it—which is a bit like performing open-heart surgery without the patient’s permission
    '''
    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name
    
    # Alternative to getters and setters, there is @property decorator
    # Can run validations when reading/writing
    '''
    Property decorators (@property) are used to define getter,
    setter, and deleter methods in a class, allowing controlled
    access to instance attributes.
    
    '''
    @property
    def name(self):
        """Getter: p.name"""
        return self._name

    @name.setter
    def name(self, new_name):
        """Setter: p.name = value"""
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        self._name = new_name
    
    @name.deleter
    def name(self):
        """Deleter: del p.name"""
        raise AttributeError("Can't delete name")
    

    #Class methods -> Does not use self
    '''
        Methods that are bound to the class and not
    the instance. They can access and modify class state that
    applies across all instances of the class. Defined using the
    @classmethod decorator.
    '''
    @classmethod
    def from_birth_year(cls, name, birth_year):
        """Alternate constructor: Person.from_birth_year"""
        current_year = 2025
        age = current_year - birth_year
        return cls(name, age)
    
    @classmethod
    def get_class_age(cls):
        return cls.species
    
    '''
    
    No self or cls.
    Just a function living in the namespace of the class.
    Good for utility functions related to the class’s domain.
    '''
    @staticmethod
    def is_valid_name(name):
        return isinstance(name, str) and name.isalpha()
    


# —————————————————————————————————————————————————————
# 1. Instantiation & Alternate Constructor
# —————————————————————————————————————————————————————
alice         = Person("Alice", 30)  
bob           = Person("Bob",   25)
alice_clone   = Person("Alice", 30)
charlie       = Person.from_birth_year("Charlie", 1997)  
#  from_birth_year is a @classmethod that computes age from birth year

# —————————————————————————————————————————————————————
# 2. Representation: __repr__ vs __str__
# —————————————————————————————————————————————————————
print(repr(alice))  
# >> Person(name='Alice', age=30, species = Homo sapiens)
# repr() is meant to be unambiguous, developer‐oriented

print(str(alice))   
# >> Alice (Homo sapiens, 30 years old)
# str()/print shows a user‑friendly summary

# —————————————————————————————————————————————————————
# 3. Comparison: __eq__ and __lt__ (used by sorted())
# —————————————————————————————————————————————————————
print(alice == bob)          # >> False  
print(alice == alice_clone)  # >> True  

people = [alice, bob, alice_clone]
print(sorted(people))        
# >> [Bob (Homo sapiens, 25 years old), 
#     Alice (Homo sapiens, 30 years old),
#     Alice (Homo sapiens, 30 years old)]
# sorted() uses __lt__ to compare ages

# —————————————————————————————————————————————————————
# 4. Container & Callable Protocols: __len__ & __call__
# —————————————————————————————————————————————————————
print(len(alice))   # >> 5  
# __len__ returns len(self.name)

print(alice())      # >> Hello, I’m Alice and I’m 30 years old.
# __call__ makes the instance “callable” and returns greet()

# —————————————————————————————————————————————————————
# 5. Context Management: __enter__ & __exit__
# —————————————————————————————————————————————————————
with Person("Bob", 25) as p:
    print(p.greet())
# >> [Entering context for Bob]
# >> Hello, I’m Bob and I’m 25 years old.
# >> [Exiting context for Bob]

# —————————————————————————————————————————————————————
# 6. Plain Getters & Setters
# —————————————————————————————————————————————————————
alice.set_name("Alicia")  
print(alice.get_name())  # >> Alicia

print(Person.get_class_age())

# —————————————————————————————————————————————————————
# 7. @property Accessors (cleaner syntax)
# —————————————————————————————————————————————————————
alice.name = "Alice"     # calls @name.setter (with validation)
print(alice.name)        # calls @property name

# —————————————————————————————————————————————————————
# 8. Static Method
# —————————————————————————————————————————————————————
print(Person.is_valid_name("Eve"))    # >> True  
print(Person.is_valid_name("Eve123")) # >> False  