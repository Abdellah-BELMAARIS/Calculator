import math


class ScientificCalculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero!")
        return a / b

    def power(self, base, exponent):
        return math.pow(base, exponent)

    def square_root(self, number):
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        return math.sqrt(number)

    def factorial(self, number):
        if number < 0:
            raise ValueError("Factorial not defined for negative numbers!")
        if not number.is_integer():
            raise ValueError("Factorial only defined for integers!")
        return math.factorial(int(number))

    def logarithm(self, number, base=10):
        if number <= 0:
            raise ValueError("Logarithm undefined for non-positive numbers!")
        if base <= 0 or base == 1:
            raise ValueError("Invalid logarithm base!")
        return math.log(number, base)

    def sine(self, angle_degrees):
        return math.sin(math.radians(angle_degrees))

    def cosine(self, angle_degrees):
        return math.cos(math.radians(angle_degrees))

    def tangent(self, angle_degrees):
        return math.tan(math.radians(angle_degrees))

    def display_menu(self):
        print("\n" + "=" * 50)
        print("        SCIENTIFIC CALCULATOR")
        print("=" * 50)
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (x^y)")
        print("6. Square Root (√)")
        print("7. Factorial (!)")
        print("8. Logarithm (log)")
        print("9. Sine (sin)")
        print("10. Cosine (cos)")
        print("11. Tangent (tan)")
        print("12. Show Calculation History")
        print("13. Clear History")
        print("14. Exit")
        print("=" * 50)

    def add_to_history(self, operation, result):
        history_entry = f"{operation} = {result}"
        self.history.append(history_entry)

    def show_history(self):
        if not self.history:
            print("\nNo calculations in history.")
        else:
            print("\nCalculation History:")
            for i, entry in enumerate(self.history, 1):
                print(f"{i}. {entry}")

    def clear_history(self):
        self.history.clear()
        print("\nHistory cleared!")

    def ask_to_continue(self):
        while True:
            continue_choice = input("\nDo you want to continue? (y/n): ").strip().lower()
            if continue_choice in ['y', 'yes']:
                return True
            elif continue_choice in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no.")

    def get_number_input(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Error: Please enter a valid number!")

    def get_integer_input(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Error: Please enter a valid integer!")

    def run(self):
        print("Welcome to the Scientific Calculator!")
        while True:
            self.display_menu()
            try:
                choice = input("\nEnter your choice (1-14): ").strip()
                if choice == '14':
                    print("Thank you for using the Scientific Calculator!")
                    break
                if choice == '12':
                    self.show_history()
                    continue
                if choice == '13':
                    self.clear_history()
                    continue

                if choice in ['1', '2', '3', '4', '5']:
                    num1 = self.get_number_input("Enter first number: ")
                    num2 = self.get_number_input("Enter second number: ")
                    if choice == '1':
                        result = self.add(num1, num2)
                        operation = f"{num1} + {num2}"
                    elif choice == '2':
                        result = self.subtract(num1, num2)
                        operation = f"{num1} - {num2}"
                    elif choice == '3':
                        result = self.multiply(num1, num2)
                        operation = f"{num1} * {num2}"
                    elif choice == '4':
                        result = self.divide(num1, num2)
                        operation = f"{num1} / {num2}"
                    elif choice == '5':
                        result = self.power(num1, num2)
                        operation = f"{num1} ^ {num2}"
                    print(f"\nResult: {operation} = {result}")
                    self.add_to_history(operation, result)
                elif choice in ['6', '7']:
                    num = self.get_number_input("Enter number: ")
                    if choice == '6':
                        result = self.square_root(num)
                        operation = f"√{num}"
                    elif choice == '7':
                        result = self.factorial(num)
                        operation = f"{int(num)}!"
                    print(f"\nResult: {operation} = {result}")
                    self.add_to_history(operation, result)
                elif choice == '8':
                    num = self.get_number_input("Enter number: ")
                    base_input = input("Enter base (default 10): ").strip()
                    base = float(base_input) if base_input else 10
                    result = self.logarithm(num, base)
                    operation = f"log_{base}({num})"
                    print(f"\nResult: {operation} = {result}")
                    self.add_to_history(operation, result)

                elif choice in ['9', '10', '11']:
                    angle = self.get_number_input("Enter angle in degrees: ")
                    if choice == '9':
                        result = self.sine(angle)
                        operation = f"sin({angle}°)"
                    elif choice == '10':
                        result = self.cosine(angle)
                        operation = f"cos({angle}°)"
                    elif choice == '11':
                        result = self.tangent(angle)
                        operation = f"tan({angle}°)"
                    print(f"\nResult: {operation} = {result:.6f}")
                    self.add_to_history(operation, f"{result:.6f}")
                else:
                    print("Invalid choice! Please select 1-14.")
                    continue
                if not self.ask_to_continue():
                    print("Thank you for using the Scientific Calculator!")
                    break
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    calc = ScientificCalculator()
    calc.run()