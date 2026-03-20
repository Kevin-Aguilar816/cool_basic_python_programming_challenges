def custom_removesuffix(text, suffix):
    if len(text) >= len(suffix) and text[-len(suffix):] == suffix:
        return text[:-len(suffix)]
    return text


text = input("Enter text: ")
suffix = input("Enter suffix to remove: ")
print("Output:", custom_removesuffix(text, suffix))
