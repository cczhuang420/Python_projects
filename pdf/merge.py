import PyPDF2
import sys

pdf_files = sys.argv[1:]
merger = PyPDF2.PdfFileMerger()

for pdf_file in pdf_files:
    merger.append(pdf_file)

merger.write('merged_files.pdf')
merger.close()
