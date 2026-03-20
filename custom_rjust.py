def custom_rjust(text, width):
    result = text
    spaces_needed = width - len(text)
    return " " * spaces_needed + result


text = input("Enter text: ")
width = int(input("Enter width: "))
print("Output:", repr(custom_rjust(text, width)))
