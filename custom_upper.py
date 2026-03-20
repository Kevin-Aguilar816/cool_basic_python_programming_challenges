def custom_upper(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result


text = input("Enter text: ")
print("Output:", custom_upper(text))
