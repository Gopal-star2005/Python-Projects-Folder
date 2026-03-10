"""
Simple Calculator
A basic calculator that performs four arithmetic operations
"""

def add(a, b):
    """Addition operation"""
    return a + b

def subtract(a, b):
    """Subtraction operation"""
    return a - b

def multiply(a, b):
    """Multiplication operation"""
    return a * b

def divide(a, b):
    """Division operation with error handling"""
    if b == 0:
        raise ValueError("Error: Division by zero is not allowed!")
    return a / b

def main():
    """Main function to run the calculator"""
    print("=" * 50)
    print("SIMPLE CALCULATOR")
    print("=" * 50)
    
    while True:
        print("\nSelect operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        
        choice = input("\nEnter choice (1/2/3/4/5): ")
        
        if choice == '5':
            print("Thank you for using the calculator!")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Please select a valid option.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                result = add(num1, num2)
                print(f"\n{num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"\n{num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"\n{num1} * {num2} = {result}")
            elif choice == '4':
                try:
                    result = divide(num1, num2)
                    print(f"\n{num1} / {num2} = {result}")
                except ValueError as e:
                    print(f"\n{e}")
        
        except ValueError:
            print("\nError: Please enter valid numbers!")
        
        print("-" * 50)

if __name__ == "__main__":
    main()
