amount=int(input("Enter the amount: "))
membership=bool(input('Enter True or False : '))

discount=0

if amount>=5000 and membership==True:
    discount=amount*20/100

elif amount>=3000 and amount<5000:
    discount=amount*10/100
else:
    discount=0

print(F"After Discount : {amount-discount:.2f} taka")