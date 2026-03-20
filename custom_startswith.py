def custom_startswith(text, prefix):
    if len(text) >= len(prefix):
        return text[:len(prefix)] == prefix
    return False
