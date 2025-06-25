def main():
    print("=== CALCULATOR APP ===")
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    
    if operator == '+': result = num1 + num2
    elif operator == '-': result = num1 - num2
    elif operator == '*': result = num1 * num2
    elif operator == '/': 
        result = num1 / num2 if num2 != 0 else "Error! Division by zero"
    else: result = "Invalid operator"
    
    print(f"Result: {result}")

if __name__ == "__main__":
    main()