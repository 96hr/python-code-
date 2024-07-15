ef divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    else:
        return f"The result is: {result}"

num1 = 10
num2 = 0

print(divide_numbers(num1, num2))

num2 = 2
print(divide_numbers(num1, num2))
