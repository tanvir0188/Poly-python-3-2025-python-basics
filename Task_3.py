#Task-1:Solve
numbers = [[2, 4,1, 5], [2,10,12], [14, 16,20]]
for group in numbers:
    print("Now checking sublist:",group)
    for n in group:
        if n % 2 == 0:
            print(f"{n} is an even number.")
    else:
            print(f"{n} is an odd number.")

#Task-2:Solve
def process_number(numbers,operation):
    value = []
    if operation == "double" :
       for n in numbers:
           value.append(n * 2)
       return value
    elif operation == "square":
        for n in numbers:
            value.append(n **2)
        return value
    elif operation  == "cube":
        for n in numbers:
            value.append(n **3)
        return value
    elif operation == "filter_number":
        for n in numbers:
          if n % 2== 0:
            value.append(n)
        return value
    elif operation == "sum":
        sum = 0
        for n in numbers:
            sum = sum+n
        return sum
    else:
        return "Invalid operation"

print(process_number([1,2,3,4],"cube"))

#Task-3:Solve
even_numbers =[2,4,6,8]
try:
    print(even_numbers[5])
except IndexError:
    print("Index 5 does not exits in the list")
