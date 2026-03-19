ten_numbers = []
print("please enter ten numbers: ")
for i in range(10):
    given_numbers = float(input(f"enter number {i+1}: "))
    ten_numbers.append(given_numbers)

first_number = ten_numbers[0]
difference = first_number
for i in range(1, 10):
    difference -= ten_numbers[i]

print(f"\nFirst number: {first_number}")
print(
    f"the difference of the first number to all the remaining numbers is: {difference}")
