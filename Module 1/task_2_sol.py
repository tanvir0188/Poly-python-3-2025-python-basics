"""
Task 2 of the function class
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
