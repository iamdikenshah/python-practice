from PyPDF2 import PdfMerger, PdfReader

reader = PdfReader("Python+Handbook.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

print(f"Text: {text} || Page count: {len(reader.pages)}")


merger = PdfMerger()
pdfs = []
names = ["pdf_merger/Leave application.pdf","pdf_merger/Resume.pdf"]

for pdf in names:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()