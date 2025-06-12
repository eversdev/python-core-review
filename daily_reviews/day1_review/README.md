copy_lines_with_keyword
A Python function that reads a text file and returns all lines containing a specified keyword.
Features include:

Uses context manager for safe file handling

Case-insensitive keyword search

Handles file-not-found errors gracefully

Usage
python
Copy
Edit
from your_module import copy_lines_with_keyword

lines = copy_lines_with_keyword('filename.txt', 'keyword')
print(lines)
Function Description
copy_lines_with_keyword(filename, keyword)

filename: path to the file to read

keyword: the word to search for in each line (case-insensitive)

Returns a list of lines containing the keyword

Error Handling
If the file does not exist, the function prints an error message and returns an empty list.


















