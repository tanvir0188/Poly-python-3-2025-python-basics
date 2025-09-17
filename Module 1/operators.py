"""
Topic: Operators in Python
In Python, operators are special symbols that perform operations
such as addition, subtraction, comparison, and logical operations on variables and values.
"""
# 1. Arithmetic Operators
# These are used to perform mathematical operations.

a = 10
b = 3
print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.333...
print("Floor Division:", a // b) # 3 (removes decimal)
print("Modulus:", a % b)         # 1 (remainder)
print("Exponent:", a ** b)       # 1000 (10^3)
# operator priority
c = 5
d = (a + b) * c / 2
print("Expression result:", d)   # (10+3)*5/2 = 32.5
#priority: (), **, *, /, //, %, +, -
P = 1000  # principal
r = 0.05  # rate (5%)
t = 3     # time in years
A = P * (1 + r) ** t
print("Compound Interest Amount:", A)


# 2. Comparison Operators

# Used to compare two values (returns True/False).

x, y = 10, 20
print("x == y:", x == y)  # False
print("x != y:", x != y)  # True
print("x > y:", x > y)    # False
print("x < y:", x < y)    # True
print("x >= 10:", x >= 10) # True
print("y <= 20:", y <= 20) # True


# -------------------------
# 3. Logical Operators
# -------------------------
# 'and', 'or', 'not' combine conditions.

p, q = True, False
print("p and q:", p and q) 
print("p or q:", p or q)   



marks = 75
attendance = 80
if (marks > 70 and attendance > 75) or marks > 90:
    print("Eligible for scholarship")
else:
    print("Not eligible")



# 4. Assignment Operators
# Used to assign values with shorthand.

x = 5
x += 3   # same as x = x + 3
print("x after +=:", x)

y = 10
y *= 2   # same as y = y * 2
print("y after *=:", y)

# 5. Membership Operators
# Used to test membership in sequences (like lists, strings).

fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)


print("mango" not in fruits)

name = "python"
print("'th' in name?", "th" in name)

data = [{"id": 1}, {"id": 2}, {"id": 3}]
print("Contains dict with id=2?", {"id": 2} in data)

# 6. Identity Operators
# 'is' and 'is not' check memory location (not just value).

# Easy Example
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a is b:", a is b)       # True (same object in memory)
print("a is c:", a is c)       # False (different objects)
print("a == c:", a == c)       # True (values are equal)

print("b is not c:", b is not c)
