from datetime import datetime
from utils import get_number
from history import history

def calculate(operator):
    number1 = get_number("\nEnter the first number: ")
    number2 = get_number("Enter the second number: ")

    while operator == "/" and number2 == 0:
        print("Cannot divide by zero...")
        number2 = get_number("Enter the second number: ")
                      
    if operator == "+":
        result = number1 + number2            
    elif operator == "-":
        result = number1 - number2            
    elif operator == "*":
        result = number1 * number2
    elif operator == "/":
        result = number1 / number2
    return number1, number2, result
            
def run_operation(operator, result_message):
    number1, number2, result = calculate(operator)
    timestamp = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    print(f"\n{result_message}: {result}\n")
    history.append(f"[{timestamp}] {number1} {operator} {number2} = {result}")
            
def addition():
    run_operation("+", "The sum of both numbers is")

def subtraction():
    run_operation("-", "The difference between both numbers is")

def multiplication():
    run_operation("*", "The product of both numbers is")

def division():
    run_operation("/", "The quotient of both numbers is")
