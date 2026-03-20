def custom_zfill(text, width):
    result = text
    zeros_needed = width - len(text)
    return "0" * zeros_needed + result
