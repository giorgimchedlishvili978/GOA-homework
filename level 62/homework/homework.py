import re

def check_text(text):
    # Regular expression to find numbers
    numbers = re.finditer(r'\d', text)
    
    # Find all indices where numbers appear
    number_indices = [match.start() for match in numbers]
    
    # If there are any numbers, return error with indices
    if number_indices:
        return f: {number_indices}"
    else:
        return ""

# Testing the function
user_input = input( ")
result = check_text(user_input)
print(result)
