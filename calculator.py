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

geo_calculator = geometryCalculator()

#Implemeted Error Handling using Try Catch
try:
    radius = float(input("Enter the radius of the circle: "))
    circle_area = geo_calculator.calculate_circle_area(radius)
    print(f"Circle area (radius {radius}): {circle_area:.2f}")  #Restricted to 2 Decimal points

    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    rectangle_area = geo_calculator.calculate_rectangle_area(length, width)
    print(f"Rectangle area (length {length}, width {width}): {rectangle_area:.2f}") #Restricted to 2 Decimal points

except ValueError as e:
    print(f"Error: {e}") 

calculator = calculator()

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print(f"Addition: {num1} + {num2} = {calculator.add(num1, num2)}")
    print(f"Subtraction: {num1} - {num2} = {calculator.subtract(num1, num2)}")
    print(f"Multiplication: {num1} * {num2} = {calculator.multiply(num1, num2)}")
    print(f"Division: {num1} / {num2} = {calculator.divide(num1, num2)}")

    num3 = float(input("Enter a number to calculate its square root: "))
    print(f"Square root of {num3}: {calculator.square_root(num3):.2f}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")