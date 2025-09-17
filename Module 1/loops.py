"""
Topic: Loops in Python
We use loops to execute some code multiple times.

In Python, we mainly use:
 - for loop
 - while loop

Both can be combined with:
 - break
 - continue
 - else clause in loops
"""

# 1. FOR Loop

# Syntax:
# for variable in iterable:
#     code block
# We are supposed to use the for loop when we know the number of iterations.

for i in range(5):  # range(5) → 0,1,2,3,4
    print("Number:", i)

for i in range(2, 6):
    print(i)   # 2, 3, 4, 5

for i in range(1, 10, 2):   # step = 2
    print(i)  # 1, 3, 5, 7, 9

for i in range(10, 0, -2):  # counting backwards
    print(i)  # 10, 8, 6, 4, 2

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)



for i in range(1, 4):   # outer loop
    for j in range(1, 4):  # inner loop
        print(f"{i} x {j} = {i*j}")
    
# Syntax:
# range(start, stop)





# 2. WHILE Loop

# Syntax:
# while condition:
#   code block

# We are supposed to use the while loop when we don't know the number of iterations in advance.
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

# Example: Calculating factorial of a number using while loop
num = 5
result = 1
while num > 0:
    result *= num
    num -= 1
print("Factorial is:", result)


# 3. BREAK and CONTINUE

# BREAK → exit the loop completely
for i in range(10):
    if i == 5:
        break
    print(i)  # prints 0–4 only

# CONTINUE → skip current iteration
for i in range(5):
    if i == 2:
        continue
    print("Number:", i)  # skips 2

# 5. INFINITE LOOPS
# A while loop without a stopping condition becomes infinite.
# Example: Uncomment to test (Ctrl+C to stop in terminal)

# while True:
#     print("This will run forever!")


# ATM PIN system (3 attempts max)

# pin = "1234"
# attempts = 0
# while attempts < 3:
#     entered = input("Enter PIN: ")
#     if entered == pin:
#         print("Access granted")
#         break
#     else:
#         print("Wrong PIN")
#         attempts += 1
# else:
#     print("Account locked after 3 failed attempts")
