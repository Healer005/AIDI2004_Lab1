def get_numeric_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.replace('.', '', 1).isdigit():  # Check if input is numeric
            return float(user_input)
        else:
            print("Please enter a numeric value.")

def add(x, y):
    result = x + y
    history.append((f"{x} + {y}", result))
    return result

def subtract(x, y):
    result = x - y
    history.append((f"{x} - {y}", result))
    return result

def multiply(x, y):
    result = x * y
    history.append((f"{x} * {y}", result))
    return result

def divide(x, y):
    if y == 0:
        result = "Cannot divide by zero"
    else:
        result = x / y
    history.append((f"{x} / {y}", result))
    return result

def display_history():
    print("\nCalculation History (Last 5):")
    for index, (calculation, result) in enumerate(history[-5:], start=1):
        print(f"{index}. {calculation} = {result}")

history = []

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Review Last 5 Calculations")
    print("6. Exit")
    
    choice = input("Enter choice (1/2/3/4/5/6): ")
    
    if choice in ('1', '2', '3', '4'):
        num1 = get_numeric_input("Enter first number: ")
        num2 = get_numeric_input("Enter second number: ")
        
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
    
    elif choice == '5':
        display_history()
    
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid Input")
