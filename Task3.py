
#task 1
numb_1 = [[2, 4, 1, 5], [2, 10, 12], [14, 16, 20]]

for i in numb_1:
    for n in i:
        print(f"{n} is an even number.") if n % 2 == 0 else print(f"{n} is an odd number.")

#task 2
def process_numbers(numbers, operation):
    if operation == "double":
        return [n * 2 for n in numbers]
    elif operation == "square":
        return [n ** 2 for n in numbers]
    elif operation == "cube":
        return [n ** 3 for n in numbers]
    elif operation == "filter_even":
        return [n for n in numbers if n % 2 == 0]
    elif operation == "sum":
        return sum(numbers)
    else:
        print("Invalid input")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(process_numbers(nums, "double"))     
print(process_numbers(nums, "square"))      
print(process_numbers(nums, "cube"))        
print(process_numbers(nums, "filter_even")) 
print(process_numbers(nums, "sum"))         
print(process_numbers(nums, "triple"))  

#task 3
even_numbers = [2, 4, 6, 8]

try:
    print(even_numbers[5])
except IndexError:
    print("Error: Index is not available!")


"""
Task 2 of the function class 'another way,
"""

def process_numbers(numbers, operation):
  num = []
  if operation == "double":
    for number in numbers:
      num.append(number*2)
    return num

  elif operation == "square":
    for number in numbers:
      num.append(number**2)
    return num

  elif operation == "cube":
    for number in numbers:
      num.append(number**3)
    return num

  elif operation == "filter_even":
    for number in numbers:
      if number %2 ==0:
        num.append(number)
    return num

  elif operation == "sum":
    sum = 0
    for number in numbers:
      sum = sum+number
    return sum

  else:
    return "Invalid operation!"



