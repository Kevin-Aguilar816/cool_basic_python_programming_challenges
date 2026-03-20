numbers = []
print("Enter numbers (non-number to stop):")

while True:
    try:
        given_numbers = float(input("Enter number: "))
        numbers.append(given_numbers)
    except ValueError:
        if numbers:
            average = sum(numbers) / len(numbers)
            print(f"Average: {average:.2f}")
            print(f"Total numbers: {len(numbers)}")
            print(f"Sum: {sum(numbers):.2f}")
