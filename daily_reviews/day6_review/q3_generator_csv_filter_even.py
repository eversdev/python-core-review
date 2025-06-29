
import csv

def filter_even_rows(rows):
    for i in rows:
        if not i: #if row is empty skip it
            continue
        try:
            if int(i[0]) % 2 == 0:
                yield i
        except ValueError:
            print("First cell of the row is not an int")
            continue
            

try:
    with open('data.csv', 'r') as file:
        rows = csv.reader(file)
        for row in filter_even_rows(rows):
            print(row)
except FileNotFoundError:
    print("This file not found, creating a new one!")
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['1', 'some data', 'other stuff'])  # odd, won't print
        writer.writerow(['2', 'even data', 'more stuff'])   # even, should print
        writer.writerow(['4', 'more even', 'stuff here'])   # even, should print
    
    
    with open('data.csv', 'r') as file:
        rows = csv.reader(file)
        for row in filter_even_rows(rows):
            print(row)

        




    

