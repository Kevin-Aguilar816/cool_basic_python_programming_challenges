numbers = []
print("Enter numbers (non-number to stop):")

while True:
    try:
        given_numbers = float(input("Enter number: "))
        numbers.append(given_numbers)
    except ValueError:
        if numbers:
            highest_number = max(numbers)
            print(f"Highest number: {highest_number}")
        else:
            print("No numbers entered.")
        break
