import json

def localize_json(file_path, localization_dict):
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    for key, value in json_data.items():
        if isinstance(value, str):
            json_data[key] = localization_dict.get(value, value)

    return json_data