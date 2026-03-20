def custom_startswith(text, prefix):
    if len(text) >= len(prefix):
        return text[:len(prefix)] == prefix
    return False


text = input("Enter text: ")
prefix = input("Enter prefix: ")
print("Output:", custom_startswith(text, prefix))
