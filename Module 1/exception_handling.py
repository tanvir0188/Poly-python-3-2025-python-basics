"""
This module demonstrates exception handling in Python using try, except, else, and finally blocks.
We use exception handling to manage errors gracefully and ensure that our program can recover from unexpected situations.
There might be cases that you can’t predict, such as a user entering invalid input or a file not being found.
You won't be able to predict every possible error, but you can handle the most common ones. And we use if else conditions to handle predictable scenarios.
For unexpected scenarios, we use exception handling. Below is an example of how to use exception handling in Python.
"""
def divide_numbers(num1, num2):
  try:
    result = num1 / num2 # Had we used if else condition here, the code will not have worked for non-numeric inputs.
  except ZeroDivisionError:
    return "Error: Cannot divide by zero."
  except TypeError:
    return "Error: Invalid input type. Please enter numbers."
  else:
    return f"The result is {result}"
  finally:
    print("Execution of divide_numbers is complete.")

"""
Here are some django scenarios where exception handling is useful:
"""
# def get_users():
#   try:
#     # Simulating a database call that might fail
#     users = fetch_users_from_database()  # This is a placeholder function
#   except DatabaseConnectionError:
#     return "Error: Unable to connect to the database."
#   except UserNotFoundError:
#     return "Error: No users found."
#   else:
#     return users
#   finally:
#     print("Execution of get_users is complete.")