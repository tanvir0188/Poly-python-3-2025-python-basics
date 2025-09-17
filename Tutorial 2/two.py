mark=75
attendance=80
if (mark >=70 and attendance>=75) or mark >=90:
   print('Eligible')
else:
   print('Not Eligible')
#task
amount = float(input(" amount is : "))
membership = input("Are you have a membership card? (yes/no): ").strip().lower() == "yes"
if amount >= 5000 and membership:
    discount =0.20
elif amount >= 3000:
    discount = 0.10
else:
    discount = 'no discount'
final_amount = amount - (amount * discount)
print("Total amount to pay: ☪ ", round(final_amount))
if discount==0:
    print('no discount')