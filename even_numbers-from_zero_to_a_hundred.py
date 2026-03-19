print("odd numbers from 0 to 100:")

number = 0
first = True

while number <= 100:
    if number % 2 != 0:
        if not first:
            print(",", end="")
        print(number, end="")
        first = False
    number += 1

print()
