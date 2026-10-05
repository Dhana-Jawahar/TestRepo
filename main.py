def calculate(a, operator, b):
    """Perform a basic arithmetic calculation."""
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    raise ValueError("Unsupported operator.")


# Change these values to test different calculations.
a = 10
operator = "*"
b = 5

result = calculate(a, operator, b)
print(f"{a} {operator} {b} = {result}")
