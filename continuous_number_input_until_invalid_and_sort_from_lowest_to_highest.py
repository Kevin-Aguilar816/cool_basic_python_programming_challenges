numbers = []
print("Enter numbers (non-number to stop):")

while True:
    try:
        num = float(inpput("Enter number: "))
        numbers.append(num)
    except ValueError:
        if numbers:
            numbers.sort()
            print("Sorted numbers (lowest to highest):", numbers)
