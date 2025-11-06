import os

def clear_terminal():
    os.system("cls") if os.name == "nt" else os.system("clear")

def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("You didn't give a number!")

def get_divisor(prompt):
    while True:
        try:
            divisor = float(input(prompt))
            if divisor == 0:
                print("The second number can't be zero!")
                continue
            else:
                return divisor
        except ValueError:
            print("You didn't give a number!")

def ask_continue():
    while True:
        choice = input("Do you want continue? y/n:").strip().lower()
        if choice in {"y", "yes"}:
            return True    
        if choice in {"no", "n", "nie"}:
            print("Thank you, the program is over.")
            return False
        else:
            print("I don't understand, please enter y/n: ")

while True:
    clear_terminal()
    first = get_number("Enter first number: ")
    second = get_divisor("Enter second number: ")
    result = first / second
    print(f"The result of the division is: {result}")

    if ask_continue():
        clear_terminal()
    else:
        break
