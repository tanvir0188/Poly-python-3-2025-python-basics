"""
A shop gives discounts based on purchase amount and membership.
If the amount is ≥ 5000 and membership is True, discount = 20%
If the amount is ≥ 3000 but < 5000, discount = 10%
If the amount is < 3000, no discount
Finally, print the final amount to pay
Hints: Use arithmetic, comparison, logical, and assignment operators
"""

# Input
amount = float(input("Enter purchase amount: "))
membership = input("Do you have membership? (yes/no): ").lower() == "yes"

# Discount calculation
if amount >= 5000 and membership:  # 20% discount
    discount = 0.20 * amount
elif amount >= 3000:               # 10% discount
    discount = 0.10 * amount
else:                              # No discount
    discount = 0

final_amount = amount - discount  # Final amount to pay
print("Final amount to pay:", final_amount)