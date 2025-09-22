def process_numbers(numbers, operation):
    lst = []
    
    if operation == 'double':
        for val in numbers:
            lst.append(val * 2)
    
    elif operation == "square":
        for val in numbers:
            lst.append(val ** 2)
    
    elif operation == "cube":
        for val in numbers:
            lst.append(val ** 3)
    
    elif operation == "filter_even":
        for val in numbers:
            if val % 2 == 0:
                lst.append(val)
    
    elif operation == "sum":
        return sum(numbers) 
    
    else:
        return 'invalid input'
    
    return lst



l = [1, 2, 3, 4, 5, 6]

print('********** "double" ***********')
print(process_numbers(l, 'double'))

print('*********** "square" **********')
print(process_numbers(l, "square"))

print('********** "cube" *************')
print(process_numbers(l, "cube"))

print('******** "filter_even" ********')
print(process_numbers(l, "filter_even"))

print('************ "sum" ************')
print(process_numbers(l, "sum"))

print('******** "invalid input" *******')
print(process_numbers(l, "Awal"))
