# OCP - Open/Closed Principle
#This principle states that software entities (classes, modules, functions, etc.)
#should be open for extension but closed for modification.

# Bad Practice
class PaymentProcessor:
    def process_payment(self, payment_type, amount):
        if payment_type == "credit_card":
            # Process credit card payment
            pass
        elif payment_type == "paypal":
            # Process PayPal payment
            pass
        # If we need to add more payment types, we have to modify this method

# Good Practice
# Polymorphism enables adding new payment methods without changing existing code
from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        # Process credit card payment
        pass
class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        # Process PayPal payment
        pass