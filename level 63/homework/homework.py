import re

def check_text(text):
    # Regular expression to find numbers and non-alphanumeric characters
    # This will look for digits or any character that is not a letter or space
    matches = re.finditer(r'[^a-zA-Z\s]', text)
    
    # Find all indices where non-alphanumeric characters or numbers appear
    error_indices = [match.start() for match in matches]
    
    # If there are any such characters, return error with indices
    if error_indices:
        return f: {error_indices}"
    else:
        return ""

# Testing the function
user_input = input("

 ")
result = check_text(user_input)
print(result)
