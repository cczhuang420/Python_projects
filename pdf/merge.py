import PyPDF2
import sys
import os


def merge_from_folder():
    input_folder = input(
        "Please provide your directory to process pdf file:  ")
    merger = PyPDF2.PdfFileMerger()
    for file in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file)
        merger.append(file_path)
    merger.write('merged_files.pdf')
    merger.close()


def merge_from_argv():
    pdf_files = sys.argv[1:]
    merger = PyPDF2.PdfFileMerger()

    for pdf_file in pdf_files:
        merger.append(pdf_file)
    merger.write('merged_files.pdf')
    merger.close()


if __name__ == "__main__":
    merge_from_folder()
    # merge_from_argv()
