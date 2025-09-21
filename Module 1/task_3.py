#Task 1:

#numb_1 = [[2, 4,1, 5], [2,10,12], [14, 16,20]]
#Check the even numbers in the list. The output should be like the following:
  #n is an even number.
  #n is an odd number

#and so on.


numb_1 = [[2, 4, 1, 5], [2, 10, 12], [14, 16, 20]]

for sublist in numb_1:       
    for n in sublist:         
        if n % 2 == 0:        
            print(f"{n} is an even number.")
        else:                 
            print(f"{n} is an odd number.")

#Task 2:

#Write a function process_numbers(numbers, operation) that:

#Takes a list of integers (numbers)

#Takes an operation string ("double", "square", "cube", "filter_even", "sum")

#Returns the result depending on the operation:

#"double" -> return a new list with each number doubled

#"square" -> return a new list with each number squared

#"cube" -> return a new list with each number cubed

#"filter_even" -> return a new list with only even numbers
#and if there is an invalid parameter given for operation name then print invalid input.



#Task 3:


#even_numbers = [2,4,6,8]

#Write a try catch block to print the fifth indexed number. 
# (hint: here the 5th index is invalid. So we should get error for that. That's why you have write a try catch block)


even_numbers = [2, 4, 6, 8]

try:
     print(even_numbers[5])
except IndexError:
     print("Error: The index you are trying to access does not exist.")
