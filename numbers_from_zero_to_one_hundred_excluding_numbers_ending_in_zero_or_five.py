print("numbers from 0 to 100 excluding all that ends on a 0 or 5:")
number = 0
first = True
count = 0

while number <= 100:
    last_digit = number % 10
    if last_digit != 0 and last_digit != 5:
        if not first:
            print(",", end=" ")
        print(number, end="")
        first = False
        count += 1

    number += 1

print()
print(f"Total numbers printed: {count}")
