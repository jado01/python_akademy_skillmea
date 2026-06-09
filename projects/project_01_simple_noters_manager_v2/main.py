from datetime import date

NOTES_FILE = "notes.txt_v2"
SEPARATOR = "--------------------"

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
    pass

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

    next_id = 1

    note_block = f"ID: {next_id}\nDate: {date_value}\nNote: {note}\nImportant: {important}\n{SEPARATOR}\n"

    with open(NOTES_FILE, "a", encoding="utf-8") as file:
        file.write(note_block)

    print(note_block)

def delete_note():
    pass


def main():
    while True:
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
            print("Invalid option. Please choose 1-4.")


if __name__ == "__main__":
    main()
