numbers = []
print("Enter numbers (non-number to stop):")

while True:
    try:
        num = float(input("Enter number: "))
        numbers.append(num)
    except ValueError:
        if numbers:
            lowest = min(numbers)
            print(f"Lowest number: {lowest}")
        else:
            print("no numbers entered.")
        break
