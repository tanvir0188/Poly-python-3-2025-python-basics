# task 1
for i in range(1, 11):
    print(f"{i} -> {'Even' if i % 2 == 0 else 'Odd'}")

#task 2
HL_Language = [ "python","java", "c++", "javascript"]
print("Python found" if "python" in HL_Language else "Not found")

#task 3
files = ["report.pdf", "image.png", "notes.txt", "slides.pdf","web page.html"]

for f in files:
    print(f"{f} -> {'PDF file' if f.endswith('.pdf') else 'PNG file' if f.endswith('.png') else 'Text file' if f.endswith('.txt') else 'Other file'}")

