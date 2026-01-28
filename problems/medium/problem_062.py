"""
Problem 62: Grade Sorter
Error Type: INDEX_ERROR
Difficulty: Medium
"""

def process_grade_data(data):
    return [value *2 for value in data]
values = [10, 20, 30]
print(process_grade_data(values))