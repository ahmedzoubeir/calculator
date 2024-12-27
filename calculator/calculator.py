def display_menu():
    print("Welcome to the Calculator App!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

def get_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1, num2

def perform_operation(choice, num1, num2):
    if choice == 1:
        return num1 + num2
    elif choice == 2:
        return num1 - num2
    elif choice == 3:
        return num1 * num2
    elif choice == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."

def main():
    # Set a default choice for Jenkins environment
    choice = 1  # You can change this based on the operation you want to test
    print(f"Choice selected: {choice}")
    # Proceed with the chosen operation
    if choice == 1:
        # perform addition or whatever operation corresponds to choice
        pass
    # Add other operations as needed...

if __name__ == "__main__":
    main()
