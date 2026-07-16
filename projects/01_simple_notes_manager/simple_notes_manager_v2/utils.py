import os
from constans import NOTES_FILE

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("Press enter to continue ...")

def get_next_id():
    ids = None

    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as file:
            content = file.read()
            if not content:
                return 1
            lines = content.splitlines()

        for line in lines:
            if line.startswith("ID:"):
                ids = line
        
        if ids is None:
            return 1
        
        last_id = ids.split()
        next_id = int(last_id[1]) + 1
        return next_id
    except FileNotFoundError:
        return 1