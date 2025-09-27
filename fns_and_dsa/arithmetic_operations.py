# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter operation ('add', 'subtract', 'multiply', 'divide'): ").strip().lower()

    
    if operation == 'add':
        return num1 + num2
    
    elif operation == 'subtract':
        return num1 - num2
    
    elif operation == 'multiply':
        return num1 * num2
    
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        return num1 / num2
    
    else:
        return f"Error: Invalid operation '{operation}'. Valid operations are 'add', 'subtract', 'multiply', 'divide'"
