def merge_dicts(dict1, dict2):
    empty_dic = {}
    for key, value in dict1.items():
        if key not in empty_dic:
            empty_dic[key] = value
        else:
            if not isinstance(empty_dic[key], list):
                empty_dic[key] = [empty_dic[key]]
            empty_dic[key].append(value) 
    for key, value in dict2.items():
        if key not in empty_dic:
            empty_dic[key] = value
        else:
            if not isinstance(empty_dic[key], list):
                empty_dic[key] = [empty_dic[key]]
            empty_dic[key].append(value)
            
    return empty_dic

        





dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}


print(merge_dicts(dict1, dict2))








