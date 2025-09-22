even_numbers = [2, 4, 6, 8]

try:
    print(even_numbers[3]) 
except IndexError:
    print('Not a valid index')
