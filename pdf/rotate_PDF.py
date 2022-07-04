import PyPDF2

file = input('Enter the PDF file path to rotate: ')

reader = PyPDF2.PdfFileReader(open(file, 'rb'))
writer = PyPDF2.PdfFileWriter()

for i in range(reader.getNumPages()):
    page = reader.getPage(i)
    page.rotateClockwise(90)
    writer.addPage(page)

with open('rotated.pdf', 'wb') as output:
    writer.write(output)
