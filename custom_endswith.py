def custom_endswith(text, suffix):
    if len(text) >= len(suffix):
        return text[-len(suffix):] == suffix
    return False


text = input("Enter text: ")
suffix = input("Enter suffix: ")
print("Output:", custom_endswith(text, suffix))
