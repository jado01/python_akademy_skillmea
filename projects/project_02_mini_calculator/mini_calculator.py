from utils import clear_terminal, pause
from history import show_history, save_history, clear_history, show_saved_history
from calculator import addition, subtraction, multiplication, division

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
