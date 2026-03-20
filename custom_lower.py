def custom_lower(text):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result


text = input("Enter text: ")
print("Output:", custom_lower(text))
