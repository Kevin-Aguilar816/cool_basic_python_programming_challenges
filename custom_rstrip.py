def custom_rstrip(text):
    i = len(text) - 1
    while i >= 0 and text[i] == ' ':
        i -= 1
    return text[:i+1]
