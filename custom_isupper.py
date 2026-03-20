def custom_isupper(text):
    for char in text:
        if char.isalpha() and not ('A' <= char <= 'Z'):
            return False
    return True


text = input("Enter text: ")
print("Output:", custom_isupper(text))
