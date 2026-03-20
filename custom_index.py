def custom_index(text, substring):
    for i in range(len(text) - len(substring) + 1):
        if text[i:i+len(substring)] == substring:
            return i
    raise ValueError("substring not found")


text = input("Enter text: ")
substr = input("Enter substring: ")
try:
    print("Output:", custom_index(text, substr))
except ValueError as e:
    print("Error:", e)
