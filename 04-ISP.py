#ISP - Interface Segregation Principle
#This principle states that no client should be forced to depend on methods it does not use.

# Bad Practice
class Worker:
    def work(self):
        pass
    def eat(self):
        pass

class HumanWorker(Worker):
    def work(self):
        # Human working
        pass
    def eat(self):
        # Human eating
        pass

class RobotWorker(Worker):
    def work(self):
        # Robot working
        pass
    def eat(self):
        # Robot does not eat, but forced to implement this method
        raise NotImplementedError("Robot does not eat")
    
# Good Practice
from abc import ABC, abstractmethod
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass
class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass
class HumanWorker(Workable, Eatable):
    def work(self):
        # Human working
        pass
    def eat(self):
        # Human eating
        pass
class RobotWorker(Workable):
    def work(self):
        # Robot working
        pass