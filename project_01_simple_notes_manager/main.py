import os
import datetime

def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

def show_menu():
    print("""====================
Simple Notes Manager
====================
1.  List Notes
2.  Add a Note
3.  Delete a Note
4.  Exit
""")

def get_choice():
    while True:
        choice = input("Choose an option (1-4): ").strip()
        if choice in {"1", "2", "3", "4"}:
            return choice
        else:
            print("Neplatna volba, skus 1-4")

def handle_list():
    print("--- Notes ---")
    data = read_notes()
    if data.strip() == "":
        print("Neexistuju ziadne poznamky")
    else:
        blocks = data.split("--------------------")
        for block in blocks:
            if block.strip() == "":
                continue

            lines = block.strip().splitlines()

            id_value = ""
            date_value = ""
            note_value = ""
            important_value = ""

            for line in lines:
                key, value = line.split(":", 1)
                key = key.strip()
                value = value.strip()
                if key == "ID":
                    id_value = value
                elif key == "Date":
                    date_value = value
                elif key == "Note":
                    note_value = value
                elif key == "Important":
                    important_value = value
            print(f"ID: {id_value}")
            print(f"Date: {date_value}")
            print(f"Note: {note_value}")
            print(f"Important: {important_value}")            
            print("--------------------")
    input("Press enter to continue...")

def read_notes():
    try:
        with open("notes.txt", "r", encoding="utf-8") as file:
            data = file.read()
            return data
    except FileNotFoundError:
        return ""
    
def handle_add():

    while True:
        note = input("Add a note: ").strip()
        if note != "":
            break
        else:
            print("Note cannot be empty, please try again.")

    while True:
        important = input("Is this note important? (yes/no): ").strip().lower()
        if important in ("yes", "y"):
            important = "yes"
            break
        elif important in ("no", "n"):
            important = "no"
            break
        else:
            print('Please enter "yes" or "no"')

    date_value = datetime.date.today().isoformat()

    data = read_notes()
    lines = data.splitlines()
    ids = []

    for line in lines:
        if line.startswith("ID:"):
            id_str = line.split(":", 1)[1].strip()
            ids.append(int(id_str))
    if not ids:
        next_id = 1
    else:
        next_id = max(ids) + 1
    
    note_block = f"ID: {next_id}\nDate: {date_value}\nNote: {note}\nImportant: {important}\n--------------------\n"
    with open("notes.txt", "a", encoding="utf-8") as file:
        file.write(note_block)
    print(f"Note added successfully (ID: {next_id}).")
    input("Press enter to continue...")

def handle_delete():
    print("This choise delete a note")
    input("Press enter to continue...")

while True:
    clear_terminal()

    show_menu()

    choice = get_choice()
    if choice == "1":
        handle_list()        
    elif choice == "2":
        handle_add()
    elif choice == "3":
        handle_delete()
    else:
        print("Good bye")
        break
