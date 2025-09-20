Task 1:
Write a program that checks numbers from 1 to 10 and
prints "Even" or "Odd" for each number using
a single line if else condition
"""
#Task 1: Solution
for x in range(1,10): # x is range value
  if x % 2 == 0:  # % is modulus,
    print(x ,"is","Even")
  else:
    print("Odd")


"""
Task 2:
Create a list of ["python", "java", "c++", "javascript"].
If "python" is in the list -> print "Python found".
Else -> print "Not found".(Use the one-line if/else style)
"""
# Task 2: Solution
my_language = ["python","java","c++","javascript"]
if "python" in my_language:
    print("my_language:","python found")
    print("my_language",type(my_language))
else:
    print("my_language:","Not found")


""""
Task 3: File Extension Check
files = ["report.pdf", "image.png", "notes.txt", "slides.pdf"]
Loop through the list and print, "PDF file found" if the file ends with .pdf.
"Other file" otherwise.
Try to use the single line if else condition
"""
#Task 3: Solution
files = ["report.pdf","image.pnf","notes.text","slides.pdf"]
for x in files:
    if x.endswith(".pdf"):
        print(x,">>","PDF file found")
    else:
        print(x,">>","Other file")