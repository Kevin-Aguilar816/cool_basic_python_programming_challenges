def custom_rindex(text, substring):
    for i in range(len(text) - len(substring), -1, -1):
        if text[i:i+len(substring)] == substring:
            return i
    raise ValueError("substring not found")


text = input("Enter text: ")
substr = input("Enter substring: ")
try:
    print("Output:", custom_rindex(text, substr))
