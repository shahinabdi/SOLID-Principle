# Initial Code - Violates SOLID Principles
# This code needs to be refactored to follow SOLID principles

class Student:
    def __init__(self, name, email, student_id):
        self.name = name
        self.email = email
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def get_letter_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'
    
    def send_email_notification(self, message):
        # Email sending logic - violates SRP
        print(f"Sending email to {self.email}: {message}")
    
    def save_to_database(self):
        # Database saving logic - violates SRP
        print(f"Saving student {self.name} to database")
    
    def generate_report(self):
        # Report generation - violates SRP
        report = f"""
        Student Report
        Name: {self.name}
        ID: {self.student_id}
        Average Grade: {self.calculate_average():.2f}
        Letter Grade: {self.get_letter_grade()}
        """
        return report

# Usage example that shows problems
student = Student("John Doe", "john@email.com", "STU001")
student.add_grade(85)
student.add_grade(90)
student.add_grade(78)

print(student.generate_report())
student.send_email_notification("Your grades have been updated")
student.save_to_database()

# Assignment: Refactor this code to follow all SOLID principles:
# 1. Single Responsibility Principle (SRP)
# 2. Open/Closed Principle (OCP) 
# 3. Liskov Substitution Principle (LSP)
# 4. Interface Segregation Principle (ISP)
# 5. Dependency Inversion Principle (DIP)