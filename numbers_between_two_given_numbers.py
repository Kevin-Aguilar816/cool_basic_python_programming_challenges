number_one = float(input("Enter first number: "))
number_two = float(input("Enter second number: "))

start = min(number_one, number_two)
end = max(number_one, number_two)

print(f"\nNumbers between {start} and {end}:")

if start.is_integer() and end.is_integer():
    start = int(start)
    end = int(end)
    current = start + 1
    while current < end:
        print(current, end=" ")
        current += 1
else:
    current = start + 0.1
    while current < end:
        print(f"{current:.1f}", end=" ")
        current += 0.1
