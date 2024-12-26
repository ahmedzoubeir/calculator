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
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice == 5:
                print("Thank you for using the Calculator App! Goodbye!")
                break
            elif choice in [1, 2, 3, 4]:
                num1, num2 = get_numbers()
                result = perform_operation(choice, num1, num2)
                print(f"The result is: {result}")
            else:
                print("Invalid choice. Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
