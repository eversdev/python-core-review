count_words() Function
What is it?
This function takes the name of a text file as input, reads the content, and counts how many times each word appears. It then returns that info as a dictionary, where the keys are the words and the values are their counts.

How does it work?
It opens the file, reads everything, and splits the text into words. Then it loops through those words, building a dictionary that keeps track of how many times each word shows up.

If the file can’t be found, it lets you know and creates a new file with a little message inside so you can add content and try again.

What should I know before using it?
The function expects a filename as a string (like "myfile.txt").

It handles the case where the file doesn’t exist by creating a new one automatically.

Returns a dictionary with word counts — if the file was empty or just created, the dictionary will be empty.

Example:

counts = count_words("example.txt")
print(counts)
# Output might look like: {'hello': 3, 'world': 2, 'python': 1}


