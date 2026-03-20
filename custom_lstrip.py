def custom_lstrip(text):
    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1
    return text[i:]


text = input("Enter text with leading spaces: ")
