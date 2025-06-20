# Student Grade Analyzer

This project defines a `Student` class that models a student with a name and a list of grades.  
It provides methods to calculate the average grade and filter grades based on defined thresholds.

## Features

- **Average Grade**: Calculates the average from the student's grade list.
- **Threshold Filtering**: Filters grades based on a first threshold using `filter()`.
- **Further Filtering**: Applies a second threshold using a list comprehension.

## Usage

```python
# Instantiate a student
s1 = Student("John", [10, 30, 50, 70, 90])

# Get the average grade
print(s1.av_grade())  # Output: 50.0

# Filter grades above threshold1 (30)
filtered = s1.filter_grade()
print(filtered)  # Output: [50, 70, 90]

# Further filter grades above threshold2 (50)
refined = s1.filter_above_threshold2(filtered)
print(refined)  # Output: [70, 90]
Thresholds
threshold1 = 30: Used in filter_grade()

threshold2 = 50: Used in filter_above_threshold2()

These are class-level attributes, meaning they are shared across all Student instances.
