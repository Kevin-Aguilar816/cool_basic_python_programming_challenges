def custom_lower(text):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result


def custom_capitalize(text):
    if len(text) == 0:
        return ""
    result = custom_lower(text)
    if len(result) > 0:
        result = result[0].upper() + result[1:]
    return result


text = input("Enter text: ")
print("Output:", custom_capitalize(text))
