numbers = []
print("Enter numbers (non-number to stop):")

while True:
    try:
        given_numbers = float(input("Enter number: "))
        numbers.append(given_numbers)
    except ValueError:
        if numbers:
            average = sum(numbers) / len(numbers)
