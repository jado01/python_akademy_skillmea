import os
from datetime import datetime

def clear_terminal():
    os.system("cls")

def menu():
    print("""==== Main menu ====
1 - Addition
2 - Subtraction
3 - Multiplication
4 - Division
5 - Show history
6 - Save history
7 - Clear history
8 - Quit
====================\n""")

def quit_program():
    print("\nGoodbye\n")

def get_number(text):
    while True:
        try:
            number = float(input(text))
            return number
        except ValueError:
            print("\nThis is not a number! Please try again.\n")

def calculate(operator):
    number1 = get_number("\nEnter the first number: ")
    
    if operator == "/":
        while True:
            number2 = get_number("Enter the second number: ")

            if number2 == 0:
                print("\nCannot divide by zero. Enter the second number again.\n")
            else:
                return number1 / number2
            
    else:
        number2 = get_number("Enter the second number: ")

        if operator == "+":
            return number1 + number2
        elif operator == "-":
            return number1 - number2
        elif operator == "*":
            return number1 * number2
            
def addition():
    result = calculate("+")
    timestamp = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    print(f"\nThe sum of both numbers is: {result}\n")
    history.append(f"[{timestamp}] Addition: {result}")

def subtraction():
    result = calculate("-")
    timestamp = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    print(f"\nThe difference between both numbers is: {result}\n")
    history.append(f"[{timestamp}] Subtraction: {result}")

def multiplication():
    result = calculate("*")
    timestamp = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    print(f"\nThe product of both numbers is: {result}\n")
    history.append(f"[{timestamp}] Multiplication: {result}")

def division():
    result = calculate("/")
    timestamp = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    print(f"\nThe quotient of both numbers is: {result}\n")
    history.append(f"[{timestamp}] Division: {result}")

def show_history():
    if not history:
        print("No history yet")
    else:
        for item in history:
            print(item)

def save_history():
    if not history:
        print("Nothing to save")

    else:
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, "history.txt")

        with open(file_path, "a") as file:
            for item in history:
                file.write(item + "\n")

        history.clear()
        print("\nHistory saved!\n")

def clear_history():
    if not history:
        print("No history to clear")
    else:
        history.clear()
        print("History cleared") 

options = {
    1 : addition,
    2 : subtraction,
    3 : multiplication,
    4 : division,
    5 : show_history,
    6 : save_history,
    7 : clear_history,
    8 : quit_program
}

history = []

while True:
    clear_terminal()
    menu()
    
    try:
        choice = int(input("Enter your choice: "))
        if choice in options:
            options[choice]()
            if choice == 8:
                break
            else:
                input("Press Enter to continue ...")
        else:
            print("\nEnter a number from 1 to 8: \n")
            input("Press Enter to continue ...")
    except ValueError:
        print('\nInvalid input. Enter a value from 1 to 8:\n')
        input("Press Enter to continue ...")
