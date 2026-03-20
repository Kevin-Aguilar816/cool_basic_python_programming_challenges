def custom_ljust(text, width):
    result = text
    while len(result) < width:
        result += " "
    return result


text = input("Enter text: ")
width = int(input("Enter width: "))
print("Output:", repr(custom_ljust(text, width)))
