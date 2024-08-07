# PDF Cleaner
This script is used to delete empty PDF files from a specified directory and log the names and paths of the deleted files.

## Installation
pip install -r requirements.txt

## Usage
1.python pdf_cleaner.py
2. Provide the directory path containing your PDF files when prompted.
3. Provide the path for the log file when prompted don't forget the file name and the extension (like this: deleted_pdfs_log.txt).

The script will check each PDF file, delete those that are empty of text, and log the names and paths of the deleted files.