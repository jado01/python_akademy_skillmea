import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_FILE = BASE_DIR / "employee_management.log"

def save_log(message):
    time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="UTF-8") as f:
        f.write(f"[{time_stamp}] {message}\n")