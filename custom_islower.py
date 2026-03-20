def custom_islower(text):
    for char in text:
        if char.isalpha() and not ('a' <= char <= 'z'):
            return False
    return True


text = input("Enter text: ")
print("Output:", custom_islower(text))
