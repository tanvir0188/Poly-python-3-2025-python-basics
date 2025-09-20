#task1
for i in range(1,11):
    print("even" if i%2==0 else"odd")


#task2
vasa = ("python,java,c,c++,javascript")
print("python" if "python" in vasa else "not found")


#task3
files = ("report.pdf","image.jpg","notes.txt","slides.pdf")
for f in files:
    print("pdf file found" if f.endswith(".pdf") else "other file")