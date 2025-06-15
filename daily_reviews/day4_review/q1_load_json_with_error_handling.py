import json


def load_json_file(filename):
    """
    This function loads data from a JSON file and returns it as a dictionary.

    If the file is not found, it creates an empty JSON file and returns an empty dictionary.
    If the JSON data is broken or invalid, it prints a message and returns an empty dictionary.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        dict: The data loaded from the JSON file or an empty dictionary if there was a problem.
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("The File was not found")
        empty_dic = {}
        with open(filename, 'w') as file:
            json.dump(empty_dic, file)
        with open(filename, 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print("Malformed file")
        data = {}
    return data

    

#data = load_json_file('data.json')
#print(data)

  
