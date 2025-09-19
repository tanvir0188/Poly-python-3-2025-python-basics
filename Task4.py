# Task 4 = Access the keys and values of the dictionaries in the list and print them
data = [
    {
        "name": "Maisha",
        "age": 22,
        "height": 5.4,
        "is_student": True,
        "skills": ["Python", "HTML"],
        "address": {"city": "Dhaka", "country": "Bangladesh"}
    },
    {
        "name": "Soummo",
        "age": 30,
        "height": 6.0,
        "is_student": False,
        "skills": ["JavaScript", "CSS"],
        "address": {"city": "Berlin", "country": "Germany"}
    }
]

# Access keys and values
for index, person in enumerate(data, start=1):
    print(f"\nDictionary {index}:")
    for key, value in person.items():
        print(f"Key: {key} -> Value: {value}")
