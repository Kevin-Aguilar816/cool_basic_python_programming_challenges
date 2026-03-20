from collections import Counter

numbers = []
print("Enter numbers (non-number to stop):")

while True:
    try:
        given_numbers = float(input("Enter number: "))
        numbers.append(given_numbers)
    except ValueError:
        if numbers:
            count = Counter(numbers)
            most_common_number = count.most_common(1)[0]
