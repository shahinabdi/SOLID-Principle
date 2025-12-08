# SRP - Single Responsibility Principle
#This principle states that a class should have only one reason to change,
#meaning it should have only one job or responsibility.

# Bad Practice
class UserManagement:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def save_to_database(self):
        # Code to save users to a database
        pass

    def send_welcome_email(self, user):
        # Code to send a welcome email
        pass

# Good Practice
class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)
class UserRepository:
    def save_to_database(self, users):
        # Code to save users to a database
        pass
class EmailService:
    def send_welcome_email(self, user):
        # Code to send a welcome email
        pass