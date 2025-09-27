# Project 01 – Simple Notes Manager

A simple terminal-based notes manager written in Python.  
This project allows the user to create, view, and delete notes, which are stored in a text file (`notes.txt`).

---

## Features

- **List notes** – Display all saved notes with their IDs.  
- **Add a note** – Create a new note with:
  - Date
  - Note text
  - Important flag (True/False)  
- **Delete a note** – Remove a note by entering its numeric ID.  
- **Exit** – Close the application.  

---

## Note format

Notes are stored in `notes.txt` in the following format:

Date: 2025-04-28
Note: Buy groceries
Important: True


Each note is separated by a dashed line (`----------------------------------`).

---

## Menu

When you run the program, you will see:

Simple Notes Manager

1 List Notes
2 Add a Note
3 Delete a Note
4 Exit
Choose an option (1–4):

---

## Example usage

**Adding a note:**

Note date: 2025-04-28
Note: Buy groceries
Is the note important: True

**Listing notes:**

Id: 1
Date: 2025-04-28
Note: Buy groceries
Important: True

**Deleting a note:**

Enter the ID of the note to delete: 1

**Exit:**

Goodbye!

---

## File handling

- On startup, the program loads notes from `notes.txt`.  
- If the file does not exist, it shows: `No notes found.`  
- New notes are appended to the file in the specified format.  
- Deleted notes are removed by rewriting the file.  

---

## Implementation tips

- Split the code into functions:
  - `read_notes()`
  - `list_notes()`
  - `add_note()`
  - `delete_note()`
  - `save_notes()`  
- Keep the interface **in English** (no diacritics).  
- Make sure the file format is preserved exactly.  

---

## Requirements

- Python 3.x  
- Works in any terminal (Windows, Linux, macOS)

---

## License

This project is created as a student exercise for **Skillmea Python Academy**.  
