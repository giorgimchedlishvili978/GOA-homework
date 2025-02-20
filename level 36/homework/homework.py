from collections import Counter

def is_anagram(test, original):
    # Normalize the strings to lowercase
    test = test.lower()
    original = original.lower()
    
    # Use Counter to count occurrences of each character
    return Counter(test) == Counter(original)
