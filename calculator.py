import math

class geometryCalculator:
    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2

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

geometric_calculator = geometryCalculator()
circle_radius = 5

circle_area = geometric_calculator.calculate_circle_area(circle_radius)

print(f"Circle area: {circle_area}")

calculator = calculator()
num1 = 15
num2 = 3

print(f"Addition: {num1} + {num2} = {calculator.add(num1, num2)}")
print(f"Subtraction: {num1} - {num2} = {calculator.subtract(num1, num2)}")
print(f"Multiplication: {num1} * {num2} = {calculator.multiply(num1, num2)}")
print(f"Division: {num1} / {num2} = {calculator.divide(num1, num2)}")
print(f"Square root of {num1}: {calculator.square_root(num1):.2f}")