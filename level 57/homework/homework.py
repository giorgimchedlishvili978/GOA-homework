def string_to_array(s):
    result = []
    word = ''
    for char in s:
        if char == ' ':
            if word:
                result.append(word)
                word = ''
        else:
            word += char
    if word:
        result.append(word)  
    return result if s else ['']