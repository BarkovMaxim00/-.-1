import json

IMPORT_FILE = 'input.json'

def task() -> float:
    filename = IMPORT_FILE
    with open(filename) as file:
        json_data = json.load(file)
    sum_values = sum([item["score"] * item["weight"] for item in json_data])

    return round(sum_values, 3)

print(task())
