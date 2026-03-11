ten_numbers = []

for i in range(10):
    entered_numbers = float(input("Give ten numbers: "))
    ten_numbers.append(entered_numbers)

given_numbers = tuple(ten_numbers)

total_sum = sum(ten_numbers)

print("the total sum of the ten given numbers is", total_sum)
