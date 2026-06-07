from datetime import datetime
from utils import clear_terminal, pause, get_number
from history import show_history, save_history, clear_history, show_saved_history
from history import history

QUIT_OPTION = 9

def menu():
    print("""===== Main menu =====
1 - Addition
2 - Subtraction
3 - Multiplication
4 - Division
5 - Show history
6 - Save history
7 - Clear history
8 - Show saved history
9 - Quit
======================\n""")

def quit_program():
    print("\nGoodbye\n")

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

options = {
    1 : addition,
    2 : subtraction,
    3 : multiplication,
    4 : division,
    5 : show_history,
    6 : save_history,
    7 : clear_history,
    8 : show_saved_history,
    9 : quit_program
}

while True:
    clear_terminal()
    menu()
    
    try:
        choice = int(input("Enter your choice: "))
        if choice in options:
            options[choice]()
            if choice == QUIT_OPTION:
                break
            else:
                pause()
        else:
            print("\nEnter a number from 1 to 9: \n")
            pause()
    except ValueError:
        print('\nInvalid input. Enter a value from 1 to 9:\n')
        pause()

