"""
Problem 162: Interest Searcher
Error Type: LOGICAL
Difficulty: Medium
"""

def check_interest(val):
    # if val = 1: # Syntax technically but often passed as logic in detailed description
    #    return True

    if val > 10:
        return 'High'
    if val > 5:
        return 'Medium'
    return 'Low' 
    # if val > 5: return Medium; if val > 10: return High. 20 -> Medium.
    
print(check_interest(20))