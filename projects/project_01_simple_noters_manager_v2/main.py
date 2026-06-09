NOTES_FILE = "notes.txt"

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
    pass

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
