#task2
mark=75
attendance=80
if (mark >=70 and attendance>=75) or mark >=90:
   print('Eligible')
else:
   print('Not Eligible')

#Task3...
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
z = x
#if x is y:
print(x is y)
#if x is z:
print(x is z)
#if z exists in y
print(3 in y)

#task 4
username = "admin"
password = "1234"
if username == "admin":
   if password == "1234":
      print("login successful")
   else:
      print("password wrong")
else:
   print("username not found")