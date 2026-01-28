"""
Problem 69: Temperature Sorter
Error Type: INDEX_ERROR
Difficulty: Medium
"""

def process_temperature_data(data):
    return{value *2 for value in data}
values = [10, 20, 30]
print(process_temperature_data(values))