import PyPDF2
import sys

pdf_files = sys.argv[1]
watermark = sys.argv[2]

pdf_files_reader = PyPDF2.PdfFileReader(open(pdf_files, 'rb'))
watermark_reader = PyPDF2.PdfFileReader(open(watermark, 'rb'))

output_file_writer = PyPDF2.PdfFileWriter()

for i in range(pdf_files_reader.getNumPages()):
    page = pdf_files_reader.getPage(i)
    page.mergePage(watermark_reader.getPage(0))
    output_file_writer.addPage(page)

with open('watermarked_out.pdf', 'wb') as file:
    output_file_writer.write(file)
