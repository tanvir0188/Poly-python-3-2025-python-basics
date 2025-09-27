# Understanding OOP, Classes, and Objects

# =============================================================================
# WHAT IS A CLASS?
# A class is a blueprint/template that defines attributes and methods
# =============================================================================

class Student:
    # Class variable (shared by all instances)
    university = "ABC University"
    
    # Constructor method (__init__) - runs when object is created
    def __init__(self, name, age, student_id):
        # Instance variables (unique to each object)
        self.name = name
        self.age = age
        self.student_id = student_id
        self.courses = []
        self.gpa = 0.0
    
    # Instance methods (behaviors/actions)
    def introduce(self):
        return f"Hi! I'm {self.name}, student ID: {self.student_id}"
    
    def enroll_course(self, course):
        self.courses.append(course)
        return f"{self.name} enrolled in {course}"
    
    def calculate_gpa(self, grades):
        if grades:
            self.gpa = sum(grades) / len(grades)
        return self.gpa
    
    def display_info(self):
        return f"""
Student Information:
Name: {self.name}
Age: {self.age}
ID: {self.student_id}
University: {self.university}
Courses: {', '.join(self.courses) if self.courses else 'None'}
GPA: {self.gpa:.2f}
        """

# =============================================================================
# CREATING OBJECTS (INSTANCES OF THE CLASS)
# Objects are actual entities created from the class blueprint
# =============================================================================

print("=== CREATING OBJECTS FROM CLASS ===")

# Creating objects (instances) of Student class
student1 = Student("Alice Johnson", 20, "STU001")
student2 = Student("Bob Smith", 19, "STU002")
student3 = Student("Carol Davis", 21, "STU003")

print("Objects created successfully!")
print(f"student1 is of type: {type(student1)}")
print(f"student2 is of type: {type(student2)}")

# =============================================================================
# ACCESSING OBJECT ATTRIBUTES AND METHODS
# =============================================================================

print("\n=== ACCESSING OBJECT ATTRIBUTES ===")

# Accessing instance attributes
print(f"Student 1 Name: {student1.name}")
print(f"Student 1 Age: {student1.age}")
print(f"Student 1 ID: {student1.student_id}")

# Accessing class attributes (same for all objects)
print(f"Student 1 University: {student1.university}")
print(f"Student 2 University: {student2.university}")

print("\n=== CALLING OBJECT METHODS ===")

# Calling methods on objects
print(student1.introduce())
print(student2.introduce())

# Each object maintains its own state
print(student1.enroll_course("Python Programming"))
print(student1.enroll_course("Data Structures"))
print(student2.enroll_course("Web Development"))

# Objects have independent data
alice_grades = [3.8, 3.9, 3.7, 4.0]
bob_grades = [3.2, 3.5, 3.4]

student1.calculate_gpa(alice_grades)
student2.calculate_gpa(bob_grades)

print(student1.display_info())
print(student2.display_info())

# =============================================================================
# DEMONSTRATING OBJECT INDEPENDENCE
# =============================================================================

print("\n=== OBJECT INDEPENDENCE ===")

# Each object has its own memory space and data
print(f"Alice's courses: {student1.courses}")
print(f"Bob's courses: {student2.courses}")
print(f"Carol's courses: {student3.courses}")

# Modifying one object doesn't affect others
student3.name = "Carol Wilson"  # Changed name
print(f"Student 3 new name: {student3.name}")
print(f"Student 1 name unchanged: {student1.name}")

# =============================================================================
# CLASS VS INSTANCE ATTRIBUTES
# =============================================================================

print("\n=== CLASS VS INSTANCE ATTRIBUTES ===")

print(f"Class attribute (university): {Student.university}")

# Changing class attribute affects all instances
Student.university = "XYZ University"
print(f"After changing class attribute:")
print(f"Student 1 university: {student1.university}")
print(f"Student 2 university: {student2.university}")

# But instance attributes are independent
student1.university = "Private College"  # Creates instance attribute
print(f"Student 1 university (instance): {student1.university}")
print(f"Student 2 university (class): {student2.university}")

# =============================================================================
# REAL-WORLD ANALOGY EXAMPLE
# =============================================================================

print("\n=== REAL-WORLD ANALOGY: CAR EXAMPLE ===")

class Car:
    # Class attribute
    wheels = 4
    
    def __init__(self, brand, model, color, year):
        # Instance attributes
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.is_running = False
        self.speed = 0
    
    # Instance methods
    def start_engine(self):
        self.is_running = True
        return f"{self.brand} {self.model} engine started!"
    
    def accelerate(self, speed_increase):
        if self.is_running:
            self.speed += speed_increase
            return f"Accelerating... Current speed: {self.speed} mph"
        return "Start the engine first!"
    
    def stop(self):
        self.is_running = False
        self.speed = 0
        return f"{self.brand} {self.model} stopped."
    
    def honk(self):
        return f"{self.brand} {self.model}: BEEP BEEP!"

# Creating car objects
my_car = Car("Honda", "Civic", "Blue", 2022)
friend_car = Car("Toyota", "Camry", "Red", 2021)
neighbor_car = Car("BMW", "X5", "Black", 2023)

print("=== CAR OBJECTS IN ACTION ===")
print(my_car.start_engine())
print(my_car.accelerate(30))
print(my_car.accelerate(20))
print(my_car.honk())

print(friend_car.start_engine())
print(friend_car.accelerate(25))
print(friend_car.honk())

# Each car object is independent
print(f"My car speed: {my_car.speed} mph")
print(f"Friend's car speed: {friend_car.speed} mph")
print(f"Neighbor's car speed: {neighbor_car.speed} mph")  # Still 0, never started

# =============================================================================
# SUMMARY DEMONSTRATION
# =============================================================================

print("\n=== SUMMARY ===")
print("""
OOP CONCEPTS DEMONSTRATED:

1. CLASS: 
   - Blueprint/template (Student, Car)
   - Defines attributes and methods
   - Can have class attributes (shared) and instance attributes

2. OBJECT: 
   - Actual instance created from class
   - Has its own memory and data
   - Can perform actions defined in the class

3. KEY POINTS:
   - Multiple objects can be created from one class
   - Each object is independent
   - Objects share methods but have separate data
   - Classes provide structure, objects provide functionality
""")

# Checking object types and relationships
print(f"student1 is instance of Student: {isinstance(student1, Student)}")
print(f"my_car is instance of Car: {isinstance(my_car, Car)}")
print(f"student1 is instance of Car: {isinstance(student1, Car)}")  # False