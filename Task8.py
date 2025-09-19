"""
Write a program that checks if a student is eligible for a scholarship.

Condition:
marks ≥ 80 and attendance ≥ 75, OR
marks ≥ 90 (regardless of attendance)
Print "Eligible" or "Not Eligible".
Use logical operators and conditions if, elif, else.
"""

# Input
marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance percentage: "))

# Check eligibility
if (marks >= 80 and attendance >= 75) or marks >= 90:
    print("Eligible")
else:
    print("Not Eligible")