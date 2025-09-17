"""
Topic: Conditions in Python
In Python, conditions are used to perform different actions based on
whether a certain condition is True or False.

We usually use:
 - if
 - if...else
 - if...elif...else
 - nested conditions
 - shorthand conditions
"""

# 1. Basic IF statement
# Syntax:
# if condition:
#     block of code

age = 20
if age >= 18:
    print("You are an adult.")   # Runs only if condition is True
"""
2. IF...ELSE
Syntax:
if condition:
    code block (if True)
else:
    code block (if False)
"""

temperature = 25
if temperature > 30:
    print("It's hot outside!")
else:
    print("The weather is nice.")   # This will run


# 3. IF...ELIF...ELSE
# Used when we need to check multiple conditions.

# Example: grading system
marks = 72
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")  
elif marks >= 50:
    print("Grade: C") # This will run
else:
    print("Grade: F")


# 4. Nested IF
# We can place if statements inside another.

# Example: Checking login system
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("User not found")

if username == "admin" and password == "1234":
    print("Login successful (flat version)")
else:
    print("Login failed (flat version)")

# 5. Logical Operators with Conditions

# We can combine multiple conditions using:
#   and -> True if both conditions are True
#   or  -> True if at least one condition is True
#   not -> Reverses True/False

# Example: Voting eligibility
age = 19
citizen = True
if age >= 18 and citizen:
    print("Eligible to vote")



# 6. Shorthand IF (single line)
x = 5
if x > 0: print("Positive number")   # One-line if



# 7. Shorthand IF...ELSE (Ternary operator)

# Syntax:
# value for true if condition else value for false

num = 10
result = "Even" if num % 2 == 0 else "Odd"
print("Number is:", result)


# 8. Using Conditions with Membership & Identity

# Membership
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list")

print('banana') if 'banana' in fruits else print('banana not found')


# 9. Real-Life example

# Student Scholarship Eligibility:
# - Must have marks > 70
# - Must have attendance >= 75
# - OR marks > 90 (automatic scholarship)

marks = 85
attendance = 80

if (marks > 70 and attendance >= 75) or marks > 90:
    print("Scholarship granted")
else:
    print("Scholarship denied")


# 10. Nested vs Flat Conditions (best practice)

# Example: Checking file extension
filename = "report.pdf"

# Nested style (less readable)
if "." in filename:
    if filename.endswith(".pdf"):
        print("It's a PDF file")

# Flat style (better readability). Apply this style as long as there aren't too many conditions
if "." in filename and filename.endswith(".pdf"):
    print("It's a PDF file (clean version)")
