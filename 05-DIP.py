#DIP - Dependency Inversion Principle
#This principle states that high-level modules should not depend on low-level modules.
#Both should depend on abstractions (e.g., interfaces).

# Bad Practice
class LightBulb:
    def turn_on(self):
        # Code to turn on the light bulb
        pass
    def turn_off(self):
        # Code to turn off the light bulb
        pass
class Switch:
    def __init__(self, bulb: LightBulb):
        self.bulb = bulb
    def operate(self, command):
        if command == "ON":
            self.bulb.turn_on()
        elif command == "OFF":
            self.bulb.turn_off()
# Here, Switch (high-level module) depends directly on LightBulb (low-level module)

# Good Practice
from abc import ABC, abstractmethod
class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass
class LightBulb(Switchable):
    def turn_on(self):
        # Code to turn on the light bulb
        pass
    def turn_off(self):
        # Code to turn off the light bulb
        pass
class Fan(Switchable):
    def turn_on(self):
        # Code to turn on the fan
        pass
    def turn_off(self):
        # Code to turn off the fan
        pass
class Switch:
    def __init__(self, device: Switchable):
        self.device = device
    def operate(self, command):
        if command == "ON":
            self.device.turn_on()
        elif command == "OFF":
            self.device.turn_off()
# Now, Switch (high-level module) depends on the Switchable interface (abstraction)