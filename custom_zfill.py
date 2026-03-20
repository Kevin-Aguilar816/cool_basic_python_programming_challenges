def custom_zfill(text, width):
    result = text
    zeros_needed = width - len(text)
    return "0" * zeros_needed + result


text = input("Enter text: ")
width = int(input("Enter width: "))
print("Output:", custom_zfill(text, width))
