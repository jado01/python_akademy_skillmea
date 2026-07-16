from utils import clear_terminal, pause
from notes import list_notes, add_note, delete_note

def show_menu():
    print("""
===========================
📃 Simple Notes Manager 📃
===========================
1️⃣  List Notes
2️⃣  Add a Note
3️⃣  Delete a Note
4️⃣  Exit
          """)
    
def get_choice():
    choice = input("Please enter the number (1-4): ").strip()
    return choice

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
            print("👋 Goodbye!")
            break
        else:
            print("\n⚠️  Invalid option. Please choose 1-4.\n")
            pause()


if __name__ == "__main__":
    main()
