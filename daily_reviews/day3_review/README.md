simple_merge()
This is a little Python function I wrote to merge two dictionaries with some simple rules:

If a key is only in one dict, just add it as is.

If a key is in both and both values are ints, add the numbers.

If a key is in both but values aren’t both ints, take the value from the second dict (dict2).

Example
python
Copy
Edit
dict1 = {'a': 1, 'b': 2, 'c': 'hello'}
dict2 = {'b': 3, 'c': 'world', 'd': 4}

print(simple_merge(dict1, dict2))
# {'a': 1, 'b': 5, 'c': 'world', 'd': 4}
How it works
Loops through each dict’s key-value pairs.

Checks if key is new or exists already.

Adds ints together if keys match and both values are ints.

Otherwise, takes the value from the second dict if keys match but values aren’t ints.

What I learned
Looping dicts with .items()

Checking types with isinstance()

Using if/elif/else to handle different cases

How to merge dictionaries with custom rules

-------------------





merge_dicts()
This function merges any number of dictionaries together with some cool rules:

If a key is only in one dict, just add it.

If a key is in multiple dicts and values are numbers (int or float), it adds them.

If the values are lists, it combines (concats) the lists.

If the values are dictionaries, it merges them recursively using the same rules.

If the values don’t match any of those, it turns them into a list to keep all values.

How it works
Takes any number of dictionaries (*dicts).

Loops through each dict, then each key-value pair inside.

Checks the existing value in the result and merges accordingly.

Keeps everything tidy by handling different types intelligently.

Why it’s handy
Useful when you want to combine lots of dictionaries with different types of data.

Handles nested dictionaries automatically.

Avoids losing data by storing conflicting values in lists.

