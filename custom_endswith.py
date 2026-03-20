def custom_endswith(text, suffix):
    if len(text) >= len(suffix):
        return text[-len(suffix):] == suffix
    return False
