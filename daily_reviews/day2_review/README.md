Sorting a List by Age Using Python
This simple Python script shows how to sort a list of people (as tuples) by their age using the built-in sorted() function and a lambda function. It sorts the list from oldest to youngest.

How to Use
Change the data list to your own list of tuples or lists, where each item has the age as the second value (index 1).

Run the script in any Python environment. No extra packages needed.

Example
python
Copy
Edit
data = [("Tom", 34), ("Dick", 28), ("Harry", 40)]
sorted_data = sorted(data, key=lambda x: x[1], reverse=True)
print(sorted_data)



Square Root with Random Number & Error Handling
This script generates a random float between 0 and 10, then calculates its square root using Python’s math and random modules. It handles errors like negative numbers or wrong types by returning a helpful message.

How to Use
Run the script — it prints the square root of a random number. To test errors, manually set num (e.g., num = -9 or num = "hello").

Example
num = -9  
print(safe_sqrt(num))  # Output: Negative number

Requirements
Standard library: Math and Random.