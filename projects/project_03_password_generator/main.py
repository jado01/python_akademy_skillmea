import os
import random

LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SPECIAL = "!@#$%^&*()-_=+[]{};:,.<>?/|\\"

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def get_password_options():
    pwd_lenght = int(input("Enter password lenght: "))
    lowercase = input("Lowercase letters? ('y' or 'n'): ")
    uppercase = input("Uppercase letters? ('y' or 'n'): ")
    numbers = input("Numbers? ('y' or 'n'): ")
    special_characters = input("Special characters? : ('y' or 'n'): ")
    options = {"pwd_lenght": pwd_lenght, "lowercase": lowercase, "uppercase": uppercase, "numbers": numbers, "specials": special_characters}
    return options

def generate_password(data):
    characters = ""
    pwd = ""

    if data["lowercase"] == "y":
        characters += LOWERCASE
    if data["uppercase"] == "y":
        characters += UPPERCASE
    if data["numbers"] == "y":
        characters += NUMBERS
    if data["specials"] == "y":
        characters += SPECIAL

    for _ in range(0, data["pwd_lenght"]):
        pwd += random.choice(characters)
    
    return pwd

def main():
    clear_terminal()
    print("""
-=-=-=-=-=-=-=-=-=-
Password Generator
-=-=-=-=-=-=-=-=-=-
1. Generate new password
2. Exit
""")
    
    while True:
        choice = input("Please enter a choice: ").strip()
        if choice == "1":
            options = get_password_options()
            pwd = generate_password(options)
            print(f" Your password is: {pwd}")

        elif choice == "2":
            break
        else:
            print("Invalid input. Please choose 1 or 2")
        


if __name__ == "__main__":
    main()
    