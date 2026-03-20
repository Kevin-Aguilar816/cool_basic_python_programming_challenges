numbers = []
print("Enter numbers (non-number to stop):")

while True:
    try:
        given_numbers = float(input("Enter a number: "))
        numbers.append(given_numbers)
    except ValueError:
        if numbers:
            numbers.sort(reverse=True)
            print("Numbers (highest to lowest):", numbers)
        else:
            print("No numbers entered.")
        break
