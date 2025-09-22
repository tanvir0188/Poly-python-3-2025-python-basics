even_numbers = [2, 4, 6, 8]

try:
    print(even_numbers[5])
except IndexError:
    print("Error: Index out of range!")
