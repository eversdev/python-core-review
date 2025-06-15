def simple_merge(dict1, dict2):
    """
    Merges two dictionaries with the following rules:

    - If a key exists in only one dictionary, add it to the result as-is.
    - If a key exists in both dictionaries and both values are integers, add them together.
    - If a key exists in both but the values are not both integers, take the value from dict2.

    Args:
        dict1 (dict): First dictionary.
        dict2 (dict): Second dictionary.

    Returns:
        dict: A new merged dictionary following the above rules.
    """
    result = {}

    # First pass: go through dict1
    for key, value in dict1.items():
        if key not in result:
            result[key] = value
        elif key in result and (isinstance(result[key], int) and isinstance(value, int)):
            result[key] += value
        elif (key in dict1 and key in dict2) and not (isinstance(dict1[key], int) and isinstance(dict2[key], int)):
            result[key] = dict2[key]

    # Second pass: go through dict2
    for key, value in dict2.items():
        if key not in result:
            result[key] = value
        elif key in result and (isinstance(result[key], int) and isinstance(value, int)):
            result[key] += value
        elif (key in dict1 and key in dict2) and not (isinstance(dict1[key], int) and isinstance(dict2[key], int)):
            result[key] = dict2[key]

    return result



dict1 = {'a': 1, 'b': 2, 'c': 'hello'}
dict2 = {'b': 3, 'c': 'world', 'd': 4}


result = simple_merge(dict1, dict2)
print(result)  
