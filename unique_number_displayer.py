from collections import Counter
ten_numbers = []
print("Enter ten numbers:")
for i in range(10):
    given_numbers = int(input(f"Number {i+1}: "))
    ten_numbers.append(given_numbers)

count = Counter(ten_numbers)
unique_numbers = [num for num, cnt in count.items() if cnt == 1]

print("\nNumbers without duplicates:", unique_numbers)
