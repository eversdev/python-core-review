JSON File Loader with Error Handling
This is a small Python script to load data from a JSON file called data.json. It handles some common problems that can happen with files:

If the file isn’t there, the script will create an empty JSON file so the program won’t crash.

If the JSON data is broken or can’t be read properly, it will print a message and use an empty dictionary instead.

The goal is to make sure the program can keep running safely even if the data file is missing or corrupted.

How to Use
Run the script in the same folder where you want data.json to be or where it already exists. If the file doesn’t exist, the script will create one.



