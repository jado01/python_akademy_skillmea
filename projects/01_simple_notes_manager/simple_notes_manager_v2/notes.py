from datetime import date
from constans import NOTES_FILE, SEPARATOR
from utils import pause, get_next_id

def list_notes():
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as file:
            content = file.read()
            if "ID:" in content:
                print(content.strip())
            else:
                print("❌  No notes found")
    except FileNotFoundError:
        print("❌  No notes found!")
    pause()


def add_note():
    while True:
        note = input("📝  Add a note: ").strip()
        if note != "":
            break
        else:
            print("⚠️  Note can't by empty!")
    
    while True:
        important = input("Is this note important? ").strip().lower()
        if important in ("yes", "y"):
            important = "Yes"    
            break
        if  important in ("no", "n"):
            important = "No"
            break
        else:
            print('⚠️ Please enter "Yes" or "No"!')
    date_value = date.today()

    next_id = get_next_id()

    note_block = f"ID: {next_id}\nDate: {date_value}\nNote: {note}\nImportant: {important}\n{SEPARATOR}\n"

    with open(NOTES_FILE, "a", encoding="utf-8") as file:
        file.write(note_block)

    print(f"\nYour added note is:\n{SEPARATOR}")
    print(note_block)
    print("✅  Note added successfully\n")
    pause()
               
def delete_note():
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as file:
            content = file.read()
            if "ID:" in content:
                notes = content.split(SEPARATOR)
                while True:
                    note_id = input("Enter note ID: ").strip()
                    remaining_notes = []
                    found = False
                    if note_id == "":
                        print("Please enter note ID. ")
                    elif not note_id.isdigit():
                        print("⚠️  Please enter a valid numeric ID. ")
                    else:
                        for note in notes:
                            if f"ID: {note_id}" in note:
                                found = True
                            else:
                                if note.strip():
                                    remaining_notes.append(note)
                        if not found:
                            print("\nNo note with this ID found.\n")
                            pause()
                            return
                        with open(NOTES_FILE, "w", encoding="utf-8") as file:
                            if remaining_notes:
                                file.write(SEPARATOR.join(remaining_notes) + SEPARATOR + "\n")
                            else:
                                file.write("")
                        print("\n✅  Note deleted successfully\n")
                        pause()
                        return
                                    
            else:
                print("❌  No notes found")
                pause()
    except FileNotFoundError:
        print("❌  No notes found")
        pause()