numbers[]
print("Enter numbers (non-number to stop):")

while True:
    try:
        num = float(input("Enter number: "))
        numbers.append(num)

        if num in numbers[:-1]:
            print("Duplicate")
        else:
            print("Unique")
