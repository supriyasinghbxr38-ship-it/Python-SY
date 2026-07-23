# Python Program to Demonstrate Different Types of Function Arguments

# 1. Required Arguments
def student(name, age):
    print("Required Arguments:")
    print("Name:", name)
    print("Age:", age)
    print()


# 2. Keyword Arguments
def employee(name, salary):
    print("Keyword Arguments:")
    print("Name:", name)
    print("Salary:", salary)
    print()


# 3. Default Arguments
def greet(name, message="Welcome!"):
    print("Default Arguments:")
    print(message, name)
    print()


# 4. Variable-Length Arguments
def total_marks(*marks):
    print("Variable-Length Arguments:")
    print("Marks:", marks)
    print("Total Marks:", sum(marks))
    print()


# Main Program
student("Alice", 20)                   # Required arguments

employee(salary=50000, name="Bob")     # Keyword arguments

greet("Charlie")                       # Uses default argument
greet("David", "Good Morning!")        # Overrides default argument

total_marks(85, 90, 78, 88, 92)        # Variable-length arguments