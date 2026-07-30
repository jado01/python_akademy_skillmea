import json
from pathlib import Path
from models.employee import Employee

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
DATA_FILE = DATA_DIR / "employees.json"

def save_employees(employees):

    employee_list = []

    for employee in employees:
        employee_data = {"employee_id": employee.employee_id, "name": employee.name, "surname": employee.surname, "position": employee.position, "salary": employee.salary}
        employee_list.append(employee_data)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(employee_list, f, indent=4, ensure_ascii=False)

def load_employees():
    if not DATA_FILE.exists():
        employee_list = []
    else:
        with open(DATA_FILE, "r", encoding="UTF-8") as f:
            employees_data = json.load(f)
            employee_list = []
            for employee_data in employees_data:
                employee = Employee(employee_data["name"], employee_data["surname"], employee_data["position"], employee_data["salary"], employee_id=employee_data["employee_id"])
                employee_list.append(employee)
    return employee_list