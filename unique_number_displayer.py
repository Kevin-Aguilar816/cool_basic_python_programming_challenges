ten_numbers = []
print("Enter ten numbers:")
for i in range(10):
    given_numbers = float(input(f"Number {i+1}: "))
    ten_numbers.append(given_numbers)

unique_numbers = []
for given_numbers in ten_numbers:
    if given_numbers not in unique_numbers:
        unique_numbers.append(given_numbers)
