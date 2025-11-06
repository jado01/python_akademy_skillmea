import os

def clear_terminal():
    os.system("cls") if os.name == "nt" else os.system("clear")

def pause(message="Press Enter to return to the main menu..."):
    input(message)

def show_menu():
    print("""
====================
Mini Calculator
====================
1 – addition
2 – subtraction
3 – multiplication
4 – division
q – quit
""")

def get_choice():
    while True:
        choice = input("Choose an option (1-4 or q): ").strip().lower()
        if choice in {"1", "2", "3", "4", "q"}:
            return choice
        else:
            print("Invalid choice. Please select 1-4 or q!")

def get_numbers():
    while True:
        try:
            first = float(input("Enter first number: "))
            break
        except ValueError:
            print("You didn't give a number!")
    
    print("-" * 20)

    while True:
        try:
            second = float(input("Enter second number: "))
            break
        except ValueError:
            print("You didn't give a number!")
    return first, second

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        print("You can't divide by zero!")
        pause()
        return None
    return a / b

# def ask_continue():
#     while True:
#         answer = input("do you wanna continue? (y/n): ").strip().lower()
#         if answer in {"y", "yes",}:
#             return True
#         elif answer in {"no", "n"}:
#             return False
#         else:
#             print("I don't understand. Please enter y or n!")

# while True:
#     clear_terminal()
#     show_menu()

#     choice = get_choice()

#     if choice == "q":
#         print("Goodbye!")
#         break

#     a, b = get_numbers()

#     if choice == "1":
#         result = add_numbers(a, b)
#     elif choice == "2":
#         result = subtract_numbers(a, b)
#     elif choice == "3":
#         result = multiply_numbers(a, b)
#     elif choice == "4":
#         result = divide_numbers(a, b)
#     else:
#         print("Invalid choice!")
#         continue

#     if result is not None:
#         print(f"Result is: {result}")
#         pause()

# --- dictionary pre operácie ---
OPS = {
    "1": ("addition", add_numbers),
    "2": ("subtraction", subtract_numbers),
    "3": ("multiplication", multiply_numbers),
    "4": ("division", divide_numbers),
}

# --- hlavný cyklus ---
while True:
    clear_terminal()
    show_menu()

    choice = get_choice()

    if choice == "q":
        print("Goodbye!")
        break

    if choice in OPS:
        label, fn = OPS[choice]     # získam názov a funkciu
        a, b = get_numbers()
        result = fn(a, b)           # zavolám funkciu dynamicky

        if result is not None:
            print(f"Result ({label}): {result:.6g}")   # pekný výstup
        pause()                     # pauza pred návratom do menu

