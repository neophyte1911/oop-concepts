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



alice = Person("Alice", 30)
bob   = Person("Bob",   25)
alice_clone = Person("Alice", 30)

# repr vs str
print(alice)               # Alice (30 years old)      ← __str__
alice                      # Person(name='Alice', age=30) ← __repr__

# equality
print(alice == bob)        # False
print(alice == alice_clone)# True

# sorting
people = [alice, bob, alice_clone]
print(sorted(people))


print(len(alice))       # 5
print(alice())          # invokes __call__

with Person("Bob", 25) as bob:
    print(bob.greet())