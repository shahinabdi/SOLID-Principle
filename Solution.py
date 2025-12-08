# Refactored Code - Following SOLID Principles
# This refactoring demonstrates all five SOLID principles

from abc import ABC, abstractmethod
from typing import List, Protocol


# ============================================================================
# 1. SINGLE RESPONSIBILITY PRINCIPLE (SRP)
# Each class has only ONE reason to change
# ============================================================================

class Student:
    """Responsible ONLY for student data management"""
    def __init__(self, name: str, email: str, student_id: str):
        self.name = name
        self.email = email
        self.student_id = student_id
        self.grades: List[float] = []
    
    def add_grade(self, grade: float) -> None:
        self.grades.append(grade)
    
    def get_grades(self) -> List[float]:
        return self.grades.copy()


class GradeCalculator:
    """Responsible ONLY for grade calculations"""
    @staticmethod
    def calculate_average(grades: List[float]) -> float:
        if not grades:
            return 0
        return sum(grades) / len(grades)


class ReportGenerator:
    """Responsible ONLY for generating reports"""
    def __init__(self, grade_evaluator: 'GradeEvaluator'):
        self.grade_evaluator = grade_evaluator
    
    def generate_report(self, student: Student) -> str:
        grades = student.get_grades()
        average = GradeCalculator.calculate_average(grades)
        letter_grade = self.grade_evaluator.get_letter_grade(average)
        
        report = f"""
        Student Report
        Name: {student.name}
        ID: {student.student_id}
        Average Grade: {average:.2f}
        Letter Grade: {letter_grade}
        """
        return report


# ============================================================================
# 2. OPEN/CLOSED PRINCIPLE (OCP)
# Open for extension, closed for modification
# ============================================================================

class GradeEvaluator(ABC):
    """Abstract base class for grade evaluation strategies"""
    @abstractmethod
    def get_letter_grade(self, average: float) -> str:
        """Evaluate grade based on average score"""
        pass


class StandardGradeEvaluator(GradeEvaluator):
    """Standard grading system"""
    def get_letter_grade(self, average: float) -> str:
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'


class HonorsGradeEvaluator(GradeEvaluator):
    """Honors grading system with stricter requirements"""
    def get_letter_grade(self, average: float) -> str:
        if average >= 93:
            return 'A'
        elif average >= 85:
            return 'B'
        elif average >= 77:
            return 'C'
        elif average >= 70:
            return 'D'
        else:
            return 'F'


class PassFailEvaluator(GradeEvaluator):
    """Pass/Fail grading system"""
    def get_letter_grade(self, average: float) -> str:
        return 'Pass' if average >= 60 else 'Fail'


# ============================================================================
# 3. LISKOV SUBSTITUTION PRINCIPLE (LSP)
# Subtypes must be substitutable for their base types
# ============================================================================

class GraduateStudent(Student):
    """Graduate student - can substitute Student anywhere"""
    def __init__(self, name: str, email: str, student_id: str, thesis_topic: str):
        super().__init__(name, email, student_id)
        self.thesis_topic = thesis_topic
    
    # Maintains the contract of the parent class
    # Does not weaken preconditions or strengthen postconditions


class UndergraduateStudent(Student):
    """Undergraduate student - can substitute Student anywhere"""
    def __init__(self, name: str, email: str, student_id: str, major: str):
        super().__init__(name, email, student_id)
        self.major = major


# ============================================================================
# 4. INTERFACE SEGREGATION PRINCIPLE (ISP)
# Clients should not depend on interfaces they don't use
# ============================================================================

class EmailSender(Protocol):
    """Small, focused interface for email functionality"""
    def send_email(self, recipient: str, message: str) -> None:
        ...


class DatabaseRepository(Protocol):
    """Small, focused interface for database operations"""
    def save(self, student: Student) -> None:
        ...


class NotificationService(Protocol):
    """Small, focused interface for notifications"""
    def notify(self, student: Student, message: str) -> None:
        ...


# Concrete implementations of segregated interfaces
class EmailNotificationService:
    """Implements ONLY email functionality"""
    def __init__(self, email_sender: EmailSender):
        self.email_sender = email_sender
    
    def notify(self, student: Student, message: str) -> None:
        self.email_sender.send_email(student.email, message)


class SMTPEmailSender:
    """Concrete email sender implementation"""
    def send_email(self, recipient: str, message: str) -> None:
        print(f"Sending email to {recipient}: {message}")


class StudentDatabaseRepository:
    """Implements ONLY database operations"""
    def save(self, student: Student) -> None:
        print(f"Saving student {student.name} to database")


# ============================================================================
# 5. DEPENDENCY INVERSION PRINCIPLE (DIP)
# Depend on abstractions, not concretions
# ============================================================================

class StudentService:
    """High-level module that depends on abstractions"""
    def __init__(
        self,
        repository: DatabaseRepository,
        notification_service: NotificationService,
        report_generator: ReportGenerator
    ):
        # Depends on abstractions (protocols/interfaces), not concrete classes
        self.repository = repository
        self.notification_service = notification_service
        self.report_generator = report_generator
    
    def process_student(self, student: Student, message: str) -> str:
        """Process student: save, notify, and generate report"""
        self.repository.save(student)
        self.notification_service.notify(student, message)
        return self.report_generator.generate_report(student)


# ============================================================================
# USAGE EXAMPLE - Demonstrating SOLID principles in action
# ============================================================================

def main():
    print("=" * 70)
    print("SOLID PRINCIPLES DEMONSTRATION")
    print("=" * 70)
    
    # Create student
    student = Student("John Doe", "john@email.com", "STU001")
    student.add_grade(85)
    student.add_grade(90)
    student.add_grade(78)
    
    # SRP: Each component has a single responsibility
    email_sender = SMTPEmailSender()
    notification_service = EmailNotificationService(email_sender)
    repository = StudentDatabaseRepository()
    
    # OCP: We can easily swap different grading systems
    standard_evaluator = StandardGradeEvaluator()
    report_generator = ReportGenerator(standard_evaluator)
    
    # DIP: High-level StudentService depends on abstractions
    student_service = StudentService(
        repository=repository,
        notification_service=notification_service,
        report_generator=report_generator
    )
    
    # Process student
    report = student_service.process_student(
        student,
        "Your grades have been updated"
    )
    print(report)
    
    print("\n" + "=" * 70)
    print("DEMONSTRATING OPEN/CLOSED PRINCIPLE")
    print("=" * 70)
    
    # OCP: Easy to extend with new grading system without modifying existing code
    honors_evaluator = HonorsGradeEvaluator()
    honors_report_generator = ReportGenerator(honors_evaluator)
    honors_service = StudentService(
        repository=repository,
        notification_service=notification_service,
        report_generator=honors_report_generator
    )
    
    print("\nHonors Grading System:")
    print(honors_service.process_student(student, "Honors grade calculated"))
    
    # Pass/Fail system
    pass_fail_evaluator = PassFailEvaluator()
    pass_fail_report_generator = ReportGenerator(pass_fail_evaluator)
    pass_fail_service = StudentService(
        repository=repository,
        notification_service=notification_service,
        report_generator=pass_fail_report_generator
    )
    
    print("\nPass/Fail Grading System:")
    print(pass_fail_service.process_student(student, "Pass/Fail grade calculated"))
    
    print("\n" + "=" * 70)
    print("DEMONSTRATING LISKOV SUBSTITUTION PRINCIPLE")
    print("=" * 70)
    
    # LSP: Graduate and Undergraduate students can substitute Student
    grad_student = GraduateStudent(
        "Jane Smith",
        "jane@email.com",
        "GRAD001",
        "Machine Learning Applications"
    )
    grad_student.add_grade(95)
    grad_student.add_grade(92)
    
    # Works seamlessly with the same service
    print("\nGraduate Student Report:")
    print(student_service.process_student(
        grad_student,
        "Graduate student grades processed"
    ))
    
    undergrad_student = UndergraduateStudent(
        "Bob Johnson",
        "bob@email.com",
        "UND001",
        "Computer Science"
    )
    undergrad_student.add_grade(88)
    undergrad_student.add_grade(82)
    
    print("\nUndergraduate Student Report:")
    print(student_service.process_student(
        undergrad_student,
        "Undergraduate student grades processed"
    ))


if __name__ == "__main__":
    main()


# ============================================================================
# SUMMARY OF SOLID PRINCIPLES APPLIED
# ============================================================================
"""
1. SINGLE RESPONSIBILITY PRINCIPLE (SRP):
   - Student: Only manages student data
   - GradeCalculator: Only calculates averages
   - ReportGenerator: Only generates reports
   - EmailNotificationService: Only handles email notifications
   - StudentDatabaseRepository: Only handles database operations

2. OPEN/CLOSED PRINCIPLE (OCP):
   - GradeEvaluator is open for extension (new grading systems)
   - Existing code is closed for modification
   - Added StandardGradeEvaluator, HonorsGradeEvaluator, PassFailEvaluator

3. LISKOV SUBSTITUTION PRINCIPLE (LSP):
   - GraduateStudent and UndergraduateStudent can substitute Student
   - They maintain the parent class contract
   - No violations of expected behavior

4. INTERFACE SEGREGATION PRINCIPLE (ISP):
   - EmailSender: Small interface for email only
   - DatabaseRepository: Small interface for database only
   - NotificationService: Small interface for notifications only
   - Clients only depend on interfaces they need

5. DEPENDENCY INVERSION PRINCIPLE (DIP):
   - StudentService depends on abstractions (Protocols)
   - Not dependent on concrete implementations
   - Easy to swap implementations via dependency injection
"""
