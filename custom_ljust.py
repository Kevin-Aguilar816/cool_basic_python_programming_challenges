def custom_ljust(text, width):
    result = text
    while len(result) < width:
        result += " "
    return result
