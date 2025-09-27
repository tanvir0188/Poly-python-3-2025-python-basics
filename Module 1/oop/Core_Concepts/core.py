# Object-Oriented Programming Concepts with Student Examples

# =============================================================================
# 1. INHERITANCE
# Definition: A mechanism where a new class inherits properties and methods 
# from an existing class, promoting code reuse and establishing relationships.
# Real-life Example: Students inherit basic human characteristics but have 
# additional specific properties like student ID, courses, grades.
# =============================================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old"
    
    def sleep(self):
        return f"{self.name} is sleeping"

class Student(Person):  # Student inherits from Person
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age)  # Call parent constructor
        self.student_id = student_id
        self.major = major
        self.grades = []
    
    def study(self):
        return f"{self.name} is studying {self.major}"
    
    def add_grade(self, grade):
        self.grades.append(grade)

class GraduateStudent(Student):  # Multi-level inheritance
    def __init__(self, name, age, student_id, major, thesis_topic):
        super().__init__(name, age, student_id, major)
        self.thesis_topic = thesis_topic
    
    def research(self):
        return f"{self.name} is researching {self.thesis_topic}"

# =============================================================================
# 2. POLYMORPHISM
# Definition: The ability of objects of different classes to be treated as 
# objects of a common base class, while maintaining their specific behaviors.
# Real-life Example: Different types of students (undergraduate, graduate, 
# international) all "study" but in different ways.
# =============================================================================

class UndergraduateStudent(Student):
    def study(self):
        return f"{self.name} is attending lectures and doing assignments"

class GraduateStudent2(Student):
    def study(self):
        return f"{self.name} is conducting research and writing papers"

class InternationalStudent(Student):
    def study(self):
        return f"{self.name} is studying while adapting to a new culture"

# Polymorphism in action
def make_students_study(students):
    for student in students:
        print(student.study())  # Same method name, different behaviors

# =============================================================================
# 3. ENCAPSULATION
# Definition: Bundling data and methods together while controlling access 
# to internal details through public, private, and protected members.
# Real-life Example: A student's personal information should be protected,
# with controlled access through proper channels.
# =============================================================================

class EncapsulatedStudent:
    def __init__(self, name, age, student_id):
        self.name = name  # Public
        self._age = age   # Protected (convention: single underscore)
        self.__student_id = student_id  # Private (name mangling: double underscore)
        self.__gpa = 0.0
    
    # Public method to access private data
    def get_student_id(self):
        return self.__student_id
    
    # Public method to modify private data with validation
    def set_gpa(self, gpa):
        if 0.0 <= gpa <= 4.0:
            self.__gpa = gpa
        else:
            raise ValueError("GPA must be between 0.0 and 4.0")
    
    def get_gpa(self):
        return self.__gpa
    
    # Protected method (for subclasses)
    def _calculate_credits(self):
        return "Calculating credits..."
    
    # Private method (internal use only)
    def __validate_data(self):
        return "Validating student data..."

# =============================================================================
# 4. ABSTRACTION
# Definition: Hiding complex implementation details while showing only 
# essential features and functionality to the user.
# Real-life Example: Students use a university portal without knowing 
# the complex database operations happening behind the scenes.
# =============================================================================

from abc import ABC, abstractmethod

class AbstractStudent(ABC):
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
    
    @abstractmethod
    def calculate_fees(self):
        pass  # Must be implemented by subclasses
    
    @abstractmethod
    def get_graduation_requirements(self):
        pass  # Must be implemented by subclasses
    
    # Concrete method (shared by all students)
    def enroll_course(self, course):
        return f"{self.name} enrolled in {course}"

class LocalStudent(AbstractStudent):
    def calculate_fees(self):
        return 5000  # Local student fees
    
    def get_graduation_requirements(self):
        return "Complete 120 credits and maintain 2.0 GPA"

class InternationalStudentAbs(AbstractStudent):
    def calculate_fees(self):
        return 15000  # International student fees
    
    def get_graduation_requirements(self):
        return "Complete 120 credits, maintain 2.5 GPA, and pass English proficiency"

# =============================================================================
# DEMONSTRATION
# =============================================================================

if __name__ == "__main__":
    print("=== INHERITANCE DEMO ===")
    student1 = Student("Alice", 20, "S001", "Computer Science")
    grad_student = GraduateStudent("Bob", 24, "G001", "AI", "Machine Learning")
    
    print(student1.introduce())  # Inherited from Person
    print(student1.study())      # Student's own method
    print(grad_student.research())  # GraduateStudent's method
    
    print("\n=== POLYMORPHISM DEMO ===")
    undergrad = UndergraduateStudent("Carol", 19, "U001", "Physics")
    grad = GraduateStudent2("Dave", 25, "G002", "Chemistry")
    international = InternationalStudent("Elena", 21, "I001", "Mathematics")
    
    students = [undergrad, grad, international]
    make_students_study(students)
    
    print("\n=== ENCAPSULATION DEMO ===")
    enc_student = EncapsulatedStudent("Frank", 22, "E001")
    print(f"Student ID: {enc_student.get_student_id()}")
    enc_student.set_gpa(3.5)
    print(f"GPA: {enc_student.get_gpa()}")
    
    # This would raise an error:
    # print(enc_student.__student_id)  # AttributeError
    
    print("\n=== ABSTRACTION DEMO ===")
    local_student = LocalStudent("Grace", "L001")
    intl_student = InternationalStudentAbs("Hassan", "I002")
    
    print(f"Local fees: ${local_student.calculate_fees()}")
    print(f"International fees: ${intl_student.calculate_fees()}")
    print(local_student.enroll_course("Data Structures"))
    
    # This would raise an error:
    # abstract_student = AbstractStudent("Test", "T001")  # TypeError