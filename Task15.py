"""
even_numbers = [2,4,6,8]

Write a try catch block to print the fifth indexed number.(hint: here the 5th
index is invalid. So we should get error for that. That's why you have write a try catch
block)
"""

even_numbers = [2, 4, 6, 8]

try:
    print(even_numbers[5])  # Trying to access the fifth index (index 5)

except IndexError:
    print("Error: The index you are trying to access does not exist.")
                            # This block runs if there is an IndexError

