def custom_capitalize(text):
    if len(text) == 0:
        return ""
    result = custom_lower(text)
    if len(result) > 0:
        result = result[0].upper() + result[1:]
    return result
