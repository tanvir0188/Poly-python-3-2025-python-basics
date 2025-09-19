"""
File Extension Check

files = ["report.pdf", "image.png", "notes.txt", "slides.pdf"]

Loop through the list and print:

"PDF file found" if the file ends with .pdf.

"Other file" otherwise.

Try to use the single line if else condition
"""

files = ["report.pdf", "image.png", "notes.txt", "slides.pdf"]

for file in files:
    print("PDF file found" if file.endswith(".pdf") else "Other file")
