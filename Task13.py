"""
numb_1 = [[2, 4,1, 5], [2,10,12], [14, 16,20]]
Check the even numbers in the list. The output should be like the following:
  n is an even number.
  n is an odd number

and so on.
"""


numb_1 = [[2, 4, 1, 5], [2, 10, 12], [14, 16, 20]]

for list in numb_1:
    for n in list:
        if n % 2 == 0:
            print(f"{n} is an even number.")
        else:
            print(f"{n} is an odd number.")
