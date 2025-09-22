files = ["report.pdf", "image.png", "notes.txt", "slides.pdf"]

for st in files:
    print(f"{'PDF file found' if st.endswith('.pdf') else 'Other file'}")

# i=0
# while i<len(files):
#     print(f"{'PDF file found' if files[i].endswith('.pdf') else 'Other file'}")
#     i+=1
