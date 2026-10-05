def calculate(a, operator, b):
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


def main():
    print("Simple Python Calculator")

    try:
        a = float(input("First number: "))
        operator = input("Operator (+, -, *, /): ").strip()
        b = float(input("Second number: "))

        result = calculate(a, operator, b)
        print(f"Result: {result}")
    except ValueError as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
