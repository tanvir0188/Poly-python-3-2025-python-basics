"""
Write a function process_numbers(numbers, operation) that:

Takes a list of integers (numbers)

Takes an operation string ("double", "square", "cube", "filter_even", "sum")

Returns the result depending on the operation:

"double" -> return a new list with each number doubled

"square" -> return a new list with each number squared

"cube" -> return a new list with each number cubed

"filter_even" -> return a new list with only even numbers
and if there is an invalid parameter given for operation name then print invalid input.
"""

nums = [1, 2, 3, 4, 5]

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
        return None

print(process_numbers(nums, "double"))       # [2, 4, 6, 8, 10]
print(process_numbers(nums, "square"))       # [1, 4, 9, 16, 25]
print(process_numbers(nums, "cube"))         # [1, 8, 27, 64, 125]
print(process_numbers(nums, "filter_even"))  # [2, 4]
print(process_numbers(nums, "sum"))          # 15
print(process_numbers(nums, "triple"))       # Invalid input
