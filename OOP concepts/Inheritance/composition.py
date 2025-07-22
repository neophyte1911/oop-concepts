'''

Composition is more like "has-a" relationship

Use cases:
    “Has‑a” or “uses‑a” relationship (e.g., Car has Engine)
    You need to mix and match behaviors or swap components
    You want to reduce coupling and increase reusability

With composition you often design to an interface (protocol) rather than a concrete class:

'''

# Component class
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return f"Engine with {self.horsepower} HP started."

# Composing Car from Engine
class Car:
    def __init__(self, make, model, engine: Engine):
        self.make   = make
        self.model  = model
        self.engine = engine  # Car *has an* Engine

    def drive(self):
        ignition = self.engine.start()
        return f"{ignition} Driving a {self.make} {self.model}"

# Usage
e = Engine(300)
c = Car("Ford", "Mustang", e)
print(c.drive())
# Engine with 300 HP started. Driving a Ford Mustang
