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
        pass

    def add_note():
        pass

    def list_note():
        pass

    def delete_note():
        pass

    def save_note():
        pass

    def load_note():
        pass

    def get_next_id():
        pass

note1 = Note(1, "2026-06-22", "kupit mlieko", True)
note2 = Note(2, "2026-06-22", "kupit chlieb", False)

note1.display()
note2.display()