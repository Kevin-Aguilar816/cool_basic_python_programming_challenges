def custom_removeprefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text


text = input("Enter text: ")
prefix = input("Enter prefix to remove: ")
