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

note1 = Note(1, "2026-06-22", "kupit mlieko", True)
note2 = Note(2, "2026-06-22", "kupit chlieb", False)

manager = NoteManager()

manager.add_note(note1)
manager.add_note(note2)

manager.list_note()

manager.delete_note(1)

manager.list_note()

print(manager.get_next_id())