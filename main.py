import math

class ScientificCalculator:
    def __init__(self):
        self.result = 0
        self.history = []
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero!"
        return a / b
    def power(self, base, exponent):
        return math.pow(base, exponent)
    def square_root(self, number):
        if number < 0:
            return "Error: Cannot calculate square root of negative number!"
        return math.sqrt(number)
    def factorial(self, number):
        if number < 0:
            return "Error: Factorial not defined for negative numbers!"
        if number == 0 or number == 1:
            return 1
        return math.factorial(number)
    def logarithm(self, number, base=10):
        if number <= 0:
            return "Error: Logarithm undefined for non-positive numbers!"
        if base <= 0 or base == 1:
            return "Error: Invalid logarithm base!"
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
        print("13. Exit")
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

    def ask_to_continue(self):
        while True:
            continue_choice = input("\nDo you want to continue? (y/n): ").strip().lower()
            if continue_choice in ['y', 'yes', '1']:
                return True
            elif continue_choice in ['n', 'no', '0']:
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no.")

    def run(self):
        print("Welcome to the Scientific Calculator!")

        while True:
            self.display_menu()

            try:
                choice = input("\nEnter your choice (1-13): ").strip()

                if choice == '13':
                    print("Thank you for using the Scientific Calculator!")
                    break

                if choice == '12':
                    self.show_history()
                    if not self.ask_to_continue():
                        print("Thank you for using the Scientific Calculator!")
                        break
                    continue

                if choice in ['1', '2', '3', '4', '5']:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))

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
                    num = float(input("Enter number: "))

                    if choice == '6':
                        result = self.square_root(num)
                        operation = f"√{num}"
                    elif choice == '7':
                        result = self.factorial(int(num))
                        operation = f"{int(num)}!"

                    print(f"\nResult: {operation} = {result}")
                    self.add_to_history(operation, result)

                elif choice == '8':
                    num = float(input("Enter number: "))
                    base = float(input("Enter base (default 10): ") or "10")
                    result = self.logarithm(num, base)
                    operation = f"log{base}({num})"
                    print(f"\nResult: {operation} = {result}")
                    self.add_to_history(operation, result)

                elif choice in ['9', '10', '11']:
                    angle = float(input("Enter angle in degrees: "))

                    if choice == '9':
                        result = self.sine(angle)
                        operation = f"sin({angle}°)"
                    elif choice == '10':
                        result = self.cosine(angle)
                        operation = f"cos({angle}°)"
                    elif choice == '11':
                        result = self.tangent(angle)
                        operation = f"tan({angle}°)"

                    print(f"\nResult: {operation} = {result:.4f}")
                    self.add_to_history(operation, f"{result:.4f}")
                else:
                    print("Invalid choice! Please select 1-13.")
                    continue
                if not self.ask_to_continue():
                    print("Thank you for using the Scientific Calculator!")
                    break

            except ValueError:
                print("Error: Please enter valid numbers!")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    calc = ScientificCalculator()
    calc.run()