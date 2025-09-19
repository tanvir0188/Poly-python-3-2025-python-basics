# Task 2 = Create a list of dictionaries with different types of variables
data = [
    {
        "name": "Maisha",                 # String
        "age": 25,                       # Integer
        "height": 5.4,                   # Float
        "is_student": True,              # Boolean
        "skills": ["Python", "HTML"],    # List
        "address": {"city": "Dhaka", "country": "Bangladesh"}  # Dictionary
    },
    {
        "name": "Siam",
        "age": 30,
        "height": 6.0,
        "is_student": False,
        "skills": ["JavaScript", "CSS"],
        "address": {"city": "Berlin", "country": "Germany"}
    },
    {
        "name": "Nazrul",
        "age": 22,
        "height": 5.7,
        "is_student": True,
        "skills": ["C++", "Java"],
        "address": {"city": "New York", "country": "USA"}
    }
]

for person in data:
    print(person)
