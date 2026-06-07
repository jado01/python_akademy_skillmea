import os

def clear_terminal():
    os.system("cls")

def pause():
    input("Press Enter to continue ...")

def get_number(text):
    while True:
        try:
            number = float(input(text))
            return number
        except ValueError:
            print("\nThis is not a number! Please try again.\n")
