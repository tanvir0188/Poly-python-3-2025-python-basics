#Task 1:

#A shop gives discounts based on purchase amount and membership.
#If the amount is ≥ 5000 and membership is True, discount = 20%
#If the amount is ≥ 3000 but < 5000, discount = 10%
#If the amount is < 3000, no discount
#Finally, print the final amount to pay
#Hints: Use arithmetic, comparison, logical, and assignment operators.

amount = 4000

is_member=True

if amount >= 5000 and is_member==True :
 result=amount*(20/100)
elif amount >= 3000 and amount<5000:
 result=amount*(10/100)
elif amount < 3000:
 result=0
print(amount-result)