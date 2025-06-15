JSON File Loader with Error Handling
This is a small Python script to load data from a JSON file called data.json. It handles some common problems that can happen with files:

If the file isn’t there, the script will create an empty JSON file so the program won’t crash.

If the JSON data is broken or can’t be read properly, it will print a message and use an empty dictionary instead.

The goal is to make sure the program can keep running safely even if the data file is missing or corrupted.

How to Use
Run the script in the same folder where you want data.json to be or where it already exists. If the file doesn’t exist, the script will create one.








# Circle Area Calculator

This is a small Python program that creates a Circle class. The class can calculate the area of a circle when you give it a radius.

## What it does

- Stores the radius of a circle
- Calculates the area using the math module for π (pi)
- Prints the area with 2 decimal places
- Shows a simple name when you print the circle object

## How to use

1. Import the Circle class in your Python file.
2. Create a Circle object by giving it a radius.
3. Call the `area()` method to get the area of the circle.

Example:

```python
from circle import Circle

my_circle = Circle(5)
print(my_circle.area())
