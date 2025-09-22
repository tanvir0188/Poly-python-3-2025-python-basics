#task 1 
# Write a program that checks numbers from 1 to 10 and prints "Even" or "Odd" for each number using a single line if else condition.

for i in range(1,11):
    print(f"{i} is even" if i%2==0 else f"{i} is odd")
    

#Task 2:
#Create a list of ["python", "java", "c++", "javascript"].

#If "python" is in the list -> print "Python found".

#Else -> print "Not found".
#(Use the one-line if/else style).

course=["python","java","c++","javascript"]
print("python found"if "python" in course else "python not found")
      
  
  
#Task 3:

#File Extension Check
#files = ["report.pdf", "image.png", "notes.txt", "slides.pdf"]
#Loop through the list and print:
#"PDF file found" if the file ends with .pdf.
#"Other file" otherwise.
#Try to use the single line if else condition
   
files=["report.pdf","image.png","notes.txt","slides.pdf"]
for file in files:
    print("PDF file found" if file.endswith(".pdf") else "outher file")