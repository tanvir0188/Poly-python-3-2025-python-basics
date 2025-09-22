#Task 1:

""""numb_1 = [[2, 4,1, 5], [2,10,12], [14, 16,20]]
Check the even numbers in the list. The output should be like the following:
  n is an even number.
  n is an odd number

and so on."""

num=[[2, 4,1, 5], [2,10,12], [14, 16,20]]
for sub_num in num:
    for  n in sub_num:
        if n%2==0:
            print(f"{n} is an even number .")
        else:
            print(f"{n} is an odd number .")
            
            
            
#Task 2:

"""Write a function process_numbers(numbers, operation) that:

Takes a list of integers (numbers)

Takes an operation string ("double", "square", "cube", "filter_even", "sum")

Returns the result depending on the operation:

"double" -> return a new list with each number doubled

"square" -> return a new list with each number squared

"cube" -> return a new list with each number cubed

"filter_even" -> return a new list with only even numbers
and if there is an invalid parameter given for operation name then print invalid input.
"""

def process_number(numbers,operation):
    if operation=="double":
        return [n * 2 for n in numbers]
    elif operation=="square":
        return[n ** 2 for n in numbers]
    elif operation == "cube":
        return [n ** 3 for n in numbers]
    elif operation== "filter_even":
        return[n for n in numbers if n%2==0 ]
    elif operation =="sum":   
        return sum(numbers)
    else:
        print("invalid number")
    
nums=[1,2,3,4,5,6,7,8,9]
print(process_number(nums,"double"))
print(process_number(nums,"square"))
print(process_number(nums,"cube"))
print(process_number(nums,"filter_even"))
print(process_number(nums,"sum"))
print(process_number(nums,"triple"))


# task 3
"""even_numbers = [2,4,6,8]

Write a try catch block to print the fifth indexed number. (hint: here the 5th index is invalid. So we should get error for that. That's why you have write a try catch block)"""

even_numbers=[2,4,6,8]
try:
    print(even_numbers[5])
except IndexError:
    print("Error : index  out of ranger .the list  has only",len(even_numbers)," elements")