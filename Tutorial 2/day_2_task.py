"""Task 1:

A shop gives discounts based on purchase amount and membership.
If the amount is ≥ 5000 and membership is True, discount = 20%
If the amount is ≥ 3000 but < 5000, discount = 10%
If the amount is < 3000, no discount
Finally, print the final amount to pay
Hints: Use arithmetic, comparison, logical, and assignment operators.
"""


amount=int(input("enter your amount :"))
is_member=bool(input("are you member (trur/false) :"))
discount=amount
if amount>=5000 and is_member==True:
    discount=amount*(20/100)
elif amount >=3000 and  is_member==True:
    discount=amount*(10/100)
elif amount < 3000 :
    discount=0
print("total discount :",discount)
print("the final amount to pay :",amount-discount)



"""Task 2:
Write a program that checks if a student is eligible for a scholarship.

Condition:
marks ≥ 80 and attendance ≥ 75, OR
marks ≥ 90 (regardless of attendance)
Print "Eligible" or "Not Eligible".
Use logical operators and conditions if, elif, else.
    """
    

marks=float(input("enter marks :"))
attendance=int(input("enter your attendence percentage :"))
if marks>=80 and attendance>=70:
    print("Eligible")
elif marks >=90:
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

num_1=[1,2,3,4]
num_2=[1,2,3,4]
num_3=num_1

print(num_1 is num_2)
print(num_1 is num_3)
print(3 in num_2)