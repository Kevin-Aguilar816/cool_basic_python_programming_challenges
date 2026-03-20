def custom_count(text, substring):
    count = 0
    start = 0
    while True:
        pos = text.find(substring, start)
        if pos == -1:
            break
        count += 1
        start = pos + 1
    return count


text = input("Enter text: ")
substr = input("Enter substring: ")
print("Output:", custom_count(text, substr))
