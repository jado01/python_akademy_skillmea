import os

HISTORY_FILE = "history.txt"

history = []

def show_history():
    if not history:
        print("No history yet")
    else:
        for item in history:
            print(item)

def get_history_path():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, HISTORY_FILE)
    return file_path

def save_history():
    if not history:
        print("Nothing to save")

    else:
        file_path = get_history_path()

        with open(file_path, "a") as file:
            for item in history:
                file.write(item + "\n")

        history.clear()
        print("\nHistory saved!\n")

def clear_history():
    if not history:
        print("No history to clear")
    else:
        history.clear()
        print("History cleared")

def show_saved_history():
    file_path = get_history_path()

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            for item in lines:
                print(item, end="")
    except FileNotFoundError:
        print("No saved history found")
