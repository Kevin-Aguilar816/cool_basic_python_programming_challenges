def custom_rstrip(text):
    i = len(text) - 1
    while i >= 0 and text[i] == ' ':
        i -= 1
    return text[:i+1]


text = input("Enter text with trailing spaces: ")
print("Output:", repr(custom_rstrip(text)))
