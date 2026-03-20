numbers[]
print("Enter numbers (non-number to stop):")

while True:
    try:
        num = float(input("Enter number: "))
        numbers.append(num)
