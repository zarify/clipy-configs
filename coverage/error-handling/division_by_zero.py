numerator = 10
denominator = 0
try:
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")