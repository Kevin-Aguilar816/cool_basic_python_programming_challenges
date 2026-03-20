def custom_center(text, width):
    spaces = width - len(text)
    left_spaces = spaces // 2
    right_spaces = spaces - left_spaces
    return " " * left_spaces + text + " " * right_spaces
