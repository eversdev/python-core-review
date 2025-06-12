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
