#LSP - Liskov Substitution Principle
#This principle states that objects of a superclass should be replaceable 
#with objects of a subclass without affecting the correctness of the program.

# Bad Practice
class Bird:
    def fly(self):
        pass
class Sparrow(Bird):
    def fly(self):
        # Sparrow can fly
        pass
class Ostrich(Bird):
    def fly(self):
        # Ostrich cannot fly, violating LSP
        raise NotImplementedError("Ostrich cannot fly")
    
# Good Practice
class Bird:
    def make_sound(self):
        pass
class FlyingBird(Bird):
    def fly(self):
        pass
class Sparrow(FlyingBird):
    def fly(self):
        # Sparrow can fly
        pass
    def make_sound(self):
        # Sparrow sound
        pass
class Ostrich(Bird):
    def make_sound(self):
        # Ostrich sound
        pass