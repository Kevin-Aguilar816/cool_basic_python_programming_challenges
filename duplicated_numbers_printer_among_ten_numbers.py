from collections import Counter
ten_numbers = []
print("Enter ten numbers:")
for i in range(10):
    given_numbers = float(input(f"Number {i+1}: "))
    ten_numbers.append(given_numbers)

count = Counter(ten_numbers)
duplicated_numbers = [given_numbers for given_numbers,
                      cnt in count.items() if cnt > 1]

print("\nNumbers with duplicates:", duplicated_numbers)
print("All numbers:", ten_numbers)
