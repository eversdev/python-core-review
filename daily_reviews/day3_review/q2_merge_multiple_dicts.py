def merge_dicts(*dicts):
    """
    Merge multiple dictionaries into one, combining values by type.

    Rules:
    - If a key is only in one dict, add it directly.
    - If a key exists in multiple dicts and values are numeric, add the numbers.
    - If values are lists, concatenate the lists.
    - If values are dictionaries, recursively merge them.
    - Otherwise, store conflicting values in a list.

    Args:
        *dicts: Variable number of dictionaries to merge.

    Returns:
        dict: A new dictionary with merged keys and combined values.
    """
    result = {}  # Initialize empty dict to hold the merged results

    # Loop over each dictionary passed as argument
    for d in dicts:
        # Loop over each key-value pair in the current dictionary
        for key, value in d.items():
            if key not in result:
                # If key is not in result, just add the key-value pair
                result[key] = value
            else:
                existing = result[key]  # Existing value in the result dict

                # If both existing and new values are numbers, add them
                if isinstance(existing, (int, float)) and isinstance(value, (int, float)):
                    result[key] = existing + value

                # If both are lists, concatenate them
                elif isinstance(existing, list) and isinstance(value, list):
                    result[key] = existing + value

                # If both are dictionaries, merge recursively
                elif isinstance(existing, dict) and isinstance(value, dict):
                    result[key] = merge_dicts(existing, value)

                else:
                    # For other cases, store all values in a list to keep them
                    if not isinstance(existing, list):
                        existing = [existing]  # Convert existing value to list if not already
                    if isinstance(value, list):
                        result[key] = existing + value  # Concatenate if new value is a list
                    else:
                        result[key] = existing + [value]  # Otherwise append new value to list

    return result




