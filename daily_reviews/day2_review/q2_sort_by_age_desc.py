data = [("Tom", 34), ("Dick", 28), ("Harry", 40)]

#print(data)

#Sort data by age (index 1) in descending order
sorted_data = sorted(data, key = lambda x: x[1], reverse=True)

print(sorted_data)