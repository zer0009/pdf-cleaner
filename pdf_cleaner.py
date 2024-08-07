import os
from PyPDF2 import PdfReader
from datetime import datetime

def is_pdf_empty(file_path):
    try:
        with open(file_path, 'rb') as pdf_file:
            reader = PdfReader(pdf_file)
            if len(reader.pages) == 0:
                return True
            for page in reader.pages:
                if page.extract_text().strip():
                    return False
        return True
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False

def search_and_delete_empty_pdfs(directory, log_file_path):
    deleted_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.pdf'):
                file_path = os.path.join(root, file)
                if is_pdf_empty(file_path):
                    try:
                        os.remove(file_path)
                        deleted_files.append(file_path)
                        print(f"Deleted: {file_path}")
                    except Exception as e:
                        print(f"Error deleting {file_path}: {e}")

    with open(log_file_path, 'a') as log_file:
        log_file.write(f"Log Date: {datetime.now()}\n")
        for deleted_file in deleted_files:
            log_file.write(f"Deleted: {deleted_file}\n")
        log_file.write("\n")

if __name__ == "__main__":
    directory_to_search = input("Enter the directory to search for empty PDFs: ")
    log_file_path = input("Enter the path for the log file (including the file name): ")

    if not os.path.isdir(directory_to_search):
        print("The provided directory does not exist.")
    else:
        search_and_delete_empty_pdfs(directory_to_search, log_file_path)
        print(f"Process completed. Check the log file at {log_file_path} for details.")