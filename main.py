class Calculator:
        def _init_(self, num1, num2):
            self.num1 = num1
            self.num2 = num2

        def add(self):
            return self.num1 + self.num2

        def subtract(self):
            return self.num1 - self.num2

        def multiply(self):
            return self.num1 * self.num2

        def divide(self):
            if self.num2 != 0:
                return self.num1 / self.num2
            else:
                return "Error: Division by zero is not allowed."

def main():
        # Ask the user to input two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Create a Calculator object
        calculator = Calculator(num1, num2)

        # Ask the user to input a mathematical operation
        operation = input("Enter the operation (+, -, *, /): ")
        while True:
            # Perform the operation and print the result
            if operation == '+':
                result = calculator.add()
                print(f"{num1} + {num2} = {result}")
            elif operation == '-':
                result = calculator.subtract()
                print(f"{num1} - {num2} = {result}")
            elif operation == '*':
                result = calculator.multiply()
                print(f"{num1} * {num2} = {result}")
            elif operation == '/':
                result = calculator.divide()
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error: Invalid operation.")
            
            # Ask the user if they want to perform another operation
            another_operation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if another_operation != 'yes':
             break
            
            #this loop reruns the main function to prompt the user to input a new mathematical values
            main()

if _name_ == "_main_":
        main()
