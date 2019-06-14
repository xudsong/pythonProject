"""读取数据"""

import json

filename = 'text_files/numbers.json'
with open(filename) as file_object:
    numbers = json.load(file_object)

print(numbers)