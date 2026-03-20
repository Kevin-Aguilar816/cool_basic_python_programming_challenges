def custom_rjust(text, width):
    result = text
    spaces_needed = width - len(text)
    return " " * spaces_needed + result
