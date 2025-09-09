"""
Creating the environment for python.
1. Search python 'python download'
2. Download the latest stable version of python.
3. After downloading python, install it(custom installation).
4. Make sure to check the box 'Add Python to PATH'.
5. After installation, open command prompt and type 'python --version' to check if python is installed correctly.
6. If the version is displayed, python is installed correctly.
7. create a folder in your desired location to save your python files.
8. Now, to run a python file, create a file with .py extension and write your code in it.
9. Open command prompt on that folder location, to do that you can type 'cmd' in the address bar of the folder and hit enter.
10. now you can open vs code by typing 'code .' in the command prompt.
11. To run the python file, type 'python filename.py' in the command prompt. for example 'python tut_1.py'
"""

# Indentation:
"""
Indentation is very important in python. It is used to define the scope of loops, functions, classes, conditions etc.
Indentation means adding spaces or tabs at the beginning of a line to indicate that it is part of a block of code.

"""
#For example:
if True:
  print("Hello, World!") # this line is indented, so it is part of the if block
  print("This is indented") # this line is also indented, so it is part of the if block
print("This is not indented") # this line is not indented, so it is not part of the if block
# if you don't indent the code, it will give an error
# for example:
"""
if True:
print("Hello, World!") # this line is not indented, so it will give an error

"""
#So always make sure to indent the code properly.

# Variables and Data Types:

# Integer type data
x=5
y=10
print(type(x))# type function is used to check the type of variable. On this case 

# String type data:
a = 'Hello world'
print('a = ' + a)
print(type(a)) # it will return <class 'str'>

# List type data:
fruits = ['apple', 'banana', 'cherry']
print(fruits)
# we can easily add obj in a list
fruits.append('jackfruit')
# we can also change a specific obj in a list
print(fruits)
fruits[0] = 'mango' # changing the first obj of the list
print(fruits) # it will return ['mango', 'banana', 'cherry', 'jackfruit']

# Tuple type data:
coordinates = (10.0, 20.0) # tuple is immutable, meaning you cannot update or change the values of a tuple.
print('before adding value:')
print(coordinates)
# coordinates.append(30.0) # this will give an error, because tuple is immutable
print('after adding value:')

print(coordinates)
"""
So if you want to change the values of a tuple, you need to create a new tuple. or you can convert the tuple to a list,
change the values and then convert it back to a tuple.
"""
coordinates = list(coordinates) # converting tuple to list
coordinates.append(30.0) # now you can add value to the list
print(type(coordinates)) # it will return <class 'list'>
coordinates = tuple(coordinates) # converting list back to tuple
print(coordinates)

print(type(coordinates)) # it will return <class 'tuple'>
# Dictionaries:

# Example of a list of dictionaries
persons = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
print(persons)
print(persons[0].keys())
print(type(persons)) # it will return <class 'list'>


"""
Python takes any kind of variable and assign the type automatically. We can even
use different types of variables in a list.
"""
persons = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, 5] # list with different types of variables
print(persons)

# Example of accessing dictionary keys
persons=[{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
print((persons[0].keys()))
print((persons[1].keys()))
# it will return dictionary keys as list
print((persons[0].values()))
print((persons[1].values()))
# it will return dictionary values as list
# we can also access specific key value
print(persons[0]['name']) # it will return 'Alice'
print(persons[0]['age']) # it will return 30
print(persons[1]['name']) # it will return 'Bob'
print(persons[1]['age']) # it will return 25
# we can also add new key value pair to the dictionary
persons[0]['city'] = 'New York' # adding new key value pair to the first dictionary
persons[1]['city'] = 'Los Angeles' # adding new key value pair to the
# we can also update the existing key value pair
print('printing the list of dictionaries before updating:')
print(persons) 
persons[0]['age'] = 31 # updating the age of the first dictionary
persons[1]['age'] = 26 # updating the age of the second dictionary
print('printing the list of dictionaries after updating')
print(persons)

"""
Tasks:
1. Create a variable of each data type and print their types.
2. Create a list of dictionaries with different types of variables and print it.
3. Declare two variables and print their sum.
4. Access the keys and values of the dictionaries in the list and print them.
5. Make a list of 3 dictionaries with name, age, and city as keys and print it.
  * Access the age key and print the sum of ages of all dictionaries in the list.
"""