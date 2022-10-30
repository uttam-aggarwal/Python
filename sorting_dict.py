def sort_dict(dict1):
    new_dict = sorted(dict1.items(), key=lambda x:x[1], reverse=True)
    converted_dict = dict(new_dict)

    return converted_dict
