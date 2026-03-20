numbers = []
print("Enter numbers (non-number to stop):")

while True:
    try:
        given_numbers = float(input("Enter a number: "))
        numbers.append(given_numbers)
