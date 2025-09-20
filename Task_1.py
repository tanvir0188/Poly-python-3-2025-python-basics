""""
Task 1:
A shop gives discounts based on purchase amount and membership.
If the amount is ≥ 5000 and membership is True, discount = 20%
If the amount is ≥ 3000 but < 5000, discount = 10%
If the amount is < 3000, no discount
Finally, print the final amount to pay
Hints: Use arithmetic, comparison, logical, and assignment operators.
"""

#Task 1: Solution
amount = 5000
membership = True
discount = 0

if amount >= 5000 and membership == True:
  discount = 0.20 #20%
if amount >= 3000 and amount < 5000:
  discount = 0.10 #10#
if amount < 3000:
  discount = 0
final_amount = amount - (amount * discount)
print("Final amount to pay:", final_amount)

""""
Task 2:
Write a program that checks if a student is eligible for a scholarship.
Condition:
marks ≥ 80 and attendance ≥ 75, OR
marks ≥ 90 (regardless of attendance)
Print "Eligible" or "Not Eligible".
Use logical operators and conditions if, elif, else.
"""
#Task 2: Solution
amount = 6000
membership = True
discount = 0

if amount >= 5000 and membership == True:
  discount = 0.20
elif amount >= 3000 and amount < 5000:
  discount = 0.10
else:
  discount = 0
final_amount = amount - (amount * discount)
print("Final amount to pay:", final_amount)

#Task 2
marks = 85
attendance = 80

if ( marks >= 80 and attendance >= 75) or marks >= 90:
  print("Eligible")
else:
  print("Not Eligible")

"""
Task 3:
nums_1 = [1, 2, 3, 4]
nums_2 = [1, 2, 3, 4]
nums_3 = nums_1
Check if nums1 is nums2 and print the result.
Check if nums1 is nums3 and print the result.
Check if number 3 exists in nums2 and print the result.
"""

#Task 3: Solution
nums_1 = [1,2,3,4]
nums_2 = [1,2,3,4]
nums_3 = nums_1

print("nums_1 is nums_2:", nums_1 is nums_2)

print("nums_1 is nums_3:", nums_1 is nums_3)

print("nums_3 is nums_2:", 3 in nums_2)