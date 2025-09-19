# List of dictionaries
people = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "Los Angeles"},
    {"name": "Charlie", "age": 28, "city": "Chicago"}
]

total_age = sum(person["age"] for person in people)

print("Sum of ages:", total_age)