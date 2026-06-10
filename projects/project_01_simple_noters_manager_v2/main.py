import os
from datetime import date

NOTES_FILE = "notes_v2.txt"
SEPARATOR = "--------------------"

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("Press enter to continue ...")

def show_menu():
    print("""
====================
Simple Notes Manager
====================
1. List Notes
2. Add a Note
3. Delete a Note
4. Exit
          """)
    
def get_choice():
    choice = input("Please enter the number: ")
    return choice

def list_notes():
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as file:
            content = file.read()
            if content:
                print(content)
            else:
                print("No notes found")
    except FileNotFoundError:
        print("No notes found!")
    pause()


def add_note():
    while True:
        note = input("Add a note: ").strip()
        if note != "":
            break
        else:
            print("Note can`t by empty!")
    
    while True:
        important = input("Is this note important? ").strip().lower()
        if important in ("yes", "y"):
            important = "Yes"    
            break
        if  important in ("no", "n"):
            important = "No"
            break
        else:
            print('Please enter "Yes" or "No"!')
    date_value = date.today()

    next_id = get_next_id()

    note_block = f"ID: {next_id}\nDate: {date_value}\nNote: {note}\nImportant: {important}\n{SEPARATOR}\n"

    with open(NOTES_FILE, "a", encoding="utf-8") as file:
        file.write(note_block)

    print(f"\nYour added note is:\n{SEPARATOR}")
    print(note_block)
    print("Note added successfully\n")
    pause()

def get_next_id():
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as file:
            content = file.read()
            if not content:
                return 1
            lines = content.splitlines()

        for line in lines:
            if line.startswith("ID:"):
                ids = line
        last_id = ids.split()
        next_id = int(last_id[1]) + 1
        return next_id
    except FileNotFoundError:
        return 1            

def delete_note():
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as file:
            content = file.read()
            if content:
                notes = content.split(SEPARATOR)
                while True:
                    note_id = input("Enter note ID: ").strip()
                    remaining_notes = []
                    found = False
                    if note_id == "":
                        print("Please enter note ID. ")
                    elif not note_id.isdigit():
                        print("Please enter a valid numeric ID. ")
                    else:
                        for note in notes:
                            if f"ID: {note_id}" in note:
                                found = True
                            else:
                                remaining_notes.append(note)
                        if not found:
                            print("\nNo note with this ID found.\n")
                            pause()
                            return
                        if found:
                            with open(NOTES_FILE, "w", encoding="utf-8") as file:
                                file.write(SEPARATOR.join(remaining_notes))
                            print("\nNote deleted successfully\n")
                            pause()
                            return
                                    
            else:
                print("No notes found")
    except FileNotFoundError:
        print("No notes found")


def main():
    while True:
        clear_terminal()
        show_menu()
        choice = get_choice()
        if choice == "1":
            list_notes()
        elif choice == "2":
            add_note()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("Goodbey")
            break
        else:
            print("\nInvalid option. Please choose 1-4.\n")
            pause()


if __name__ == "__main__":
    main()
