from PyPDF2 import PdfFileWriter, PdfFileReader
from getpass import getpass

pdf_writer = PdfFileWriter()
pdf = PdfFileReader("Новый документ.pdf")

for page in range(pdf.numPages):
    pageObj = pdf.getPage(page)
    pdf_writer.add_page(pdf.pages[page])

password = getpass(prompt="введите пароль:")
pdf_writer.encrypt(password)

with open('protected.pdf', 'wb') as file:
    pdf_writer.write(file)