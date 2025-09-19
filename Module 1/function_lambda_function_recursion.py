
# A function is a reusable block of code that performs a specific task. It helps to make your code modular and readable.
# Syntax:
def function_name(parameters):
  """
  Optional docstring explaining the function
  """
  # Code block
  return result  # Optional

# Function to add two numbers
def add_numbers(a, b):
  return a + b

result = add_numbers(5, 10)
print("Sum:", result)  # Output: Sum: 15

# Function with default parameters
def greet(name="Guest"):
  print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet()         # Output: Hello, Guest!

# Lambda function (anonymous function)
#syntax:
#lambda arguments: expression


# Lambda to add two numbers
add = lambda x, y: x + y
print(add(5, 10))  # Output: 15




def my_func(n):
  return lambda a : a * n

my_doubler = my_func(2)

print(my_doubler(11))

# map(function, iterable)


numbers = [1, 2, 3, 4, 5]

# Double each number using map
doubled = map(lambda x: x*2, numbers)

# Convert map object to list
doubled_list = list(doubled)
print(doubled)

"""
When to use lambda:

When you need a small one-liner function.

When you need a function as an argument to another function (map, filter, sort, etc.).

Avoid lambda for complex multi-line logic.
"""

def factorial_iterative(n):
  result = 1
  for i in range(2, n + 1):
    result *= i
  return result
print(factorial_iterative(5))

def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  return n * factorial(n - 1)

print(factorial(5)) # Output: 120

