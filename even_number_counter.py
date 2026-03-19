ten_numbers = []

for i in range(10):
    given_numbers = float(input("enter ten numbers: "))
    ten_numbers.append(given_numbers)

entered_numbers = tuple(ten_numbers)

even_number_count = 0

for i in entered_numbers:
    if i % 2 == 0:
        even_number_count += 1

print("count of even numbers:", even_number_count)
