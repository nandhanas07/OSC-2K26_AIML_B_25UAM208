"""
Problem 55: Budget Sorter
Error Type: INDEX_ERROR
Difficulty: Medium
"""

def process_budget_data(data):
   return[value *2 for value in data]
values = [10, 20, 30]
print(process_budget_data(values))