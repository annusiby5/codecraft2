# Function to perform calculation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed!"
        else:
            return num1 / num2
    else:
        return "Invalid operation!"

# Main program
def main():
    print("🧮 Simple Python Calculator 🧮")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        result = calculate(num1, num2, operation)
        print("Result:", result)
        
    except ValueError:
        print("Error: Please enter valid numbers.")

# Run the calculator
main()
