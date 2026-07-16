import os
from datetime import date
class Note():
    def __init__(self, note_id, date, note, important):
        self.note_id = note_id
        self.date = date
        self.note = note
        self.important = important

    def display(self):
        if self.important:
            importancy = "Yes"
        else:
            importancy = "No"

        print(f"ID: {self.note_id}\nDate: {self.date}\nNote: {self.note}\nImportant: {importancy}")
        print("--------------------")

class NoteManager():
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)
    
    def create_note(self, note, important):
        new_id = self.get_next_id()
        current_date = date.today()

        new_note = Note(new_id, current_date, note, important)

        self.add_note(new_note)
        
    def list_note(self):
        for note in self.notes:
            note.display()
            

    def delete_note(self, search_id):
        found = False
        for note in self.notes:
            if note.note_id == search_id:
                found = True
                self.notes.remove(note)
                print(f"Note ID: {note.note_id} deleted")
        if found == False:
            print("ID not found!")

    def save_note(self):
        pass        

    def load_note(self):
        pass

    def get_next_id(self):
        new_id = 0
        if self.notes == []:
            new_id = 1
        else:
            for note in self.notes:
                if note.note_id > new_id:
                    new_id = note.note_id
            new_id += 1
        return new_id

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("Press enter to continue ...")

def show_menu():
    print("""
=======================
= Simpe Notes Manager =
=======================
1. Add a note
2. List notes
3. Delete a note
4. Exit
          """)

def get_choice():
    choice = input("Please enter the number 1-4: ").strip()
    return choice

def main():
    manager = NoteManager()

    while True:
        clear_terminal()
        show_menu()
        choice = get_choice()
        if choice == "1":
            note_text = input("Enter note: ")
            important = input("Important? (y/n): ").strip().lower() == "y"
            manager.create_note(note_text, important)
            pause()
        elif choice == "2":
            manager.list_note()
            pause()
        elif choice == "3":
            search_id = int(input("Enter note ID to delete: "))
            manager.delete_note(search_id)
            pause()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("\n⚠️  Invalid option. Please choose 1-4.\n")
            pause()
    

if __name__ == "__main__":
    main()
