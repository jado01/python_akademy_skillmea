import os

def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

def show_menu():
    print("""Simple Notes Manager
====================
1.  List Notes
2.  Add a Note
3.  Delete a Note
4.  Exit""")

def get_choice():
    while True:
        choice = input("Choose an option (1-4): ").strip()
        if choice in {"1", "2", "3", "4"}:
            return choice
        else:
            print("Neplatna volba, skus 1-4")

def handle_list():
    print("List (WIP)")
    data = read_notes()
    if data.strip() == "":
        print("Neexistuju ziadne poznamky")
    else:
        blocks = data.split("--------------------")
        for block in blocks:
            print(">>>NOvy BLOK<<")
            print(block)
            print("--------------------")

def read_notes():
    try:
        with open("notes.txt", "r", encoding="utf-8") as file:
            data = file.read()
            return data
    except FileNotFoundError:
        return ""

while True:
    clear_terminal()

    show_menu()

    choice = get_choice()
    if choice == "1":
        handle_list()
        input("Stlac enter")
    elif choice == "2":
        print("ADD note")
    elif choice == "3":
        print("Delete a note")
    else:
        break