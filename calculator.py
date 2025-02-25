import math

class geometryCalculator:
    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2

    def calculate_rectangle_area(self, length, width):
        return length * width

class calculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b):
        if b == 0: raise ValueError("Cannot divide by zero.")
        return round(a / b, 2)
    def square_root(self, x):
        if x < 0: raise ValueError("Cannot compute square root of a negative number.")
        return math.sqrt(x)

def main():
    while True:
        choice = input("\nSelect Calculator:\n1. Geometry\n2. Basic\n3. Exit\nEnter your choice (1/2/3): ")
        if choice == '1':
            geo_calculator = geometryCalculator()
            geo_choice = input("1. Circle Area\n2. Rectangle Area\nEnter your choice (1/2): ")
            if geo_choice == '1':
                radius = float(input("Enter radius: "))
                print(f"Circle area: {geo_calculator.calculate_circle_area(radius):.2f}")
            elif geo_choice == '2':
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                print(f"Rectangle area: {geo_calculator.calculate_rectangle_area(length, width):.2f}")
        elif choice == '2':
            calculator = calculator()
            calc_choice = input("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Square Root\nEnter your choice (1-5): ")
            if calc_choice in ['1', '2', '3', '4']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                operations = {
                    '1': calculator.add,
                    '2': calculator.subtract,
                    '3': calculator.multiply,
                    '4': calculator.divide
                }
                print(f"Result: {operations[calc_choice](num1, num2)}")
            elif calc_choice == '5':
                num = float(input("Enter number for square root: "))
                try:
                    print(f"Square root: {calculator.square_root(num):.2f}")
                except ValueError as e:
                    print(f"Error: {e}")
        elif choice == '3':
            print("Exiting.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()