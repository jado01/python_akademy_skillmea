import json
from pathlib import Path
from models.employee import Employee
from models.organization import Manager
from models.organization import Leader
from models.organization import Department

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
DATA_FILE = DATA_DIR / "employees.json"
ORGANIZATION_FILE = DATA_DIR / "organization_structure.json"

def save_employees(employees):

    employee_list = []

    for employee in employees:

        employee_data = {"employee_id": employee.employee_id, "employee_type": employee.employee_type, "name": employee.name, "surname": employee.surname, "position": employee.position, "salary": employee.salary}
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
                employee_type = employee_data["employee_type"]

                if employee_type == "leader":
                    employee = Leader(employee_data["name"], employee_data["surname"], employee_data["position"], employee_data["salary"], employee_id=employee_data["employee_id"])

                elif employee_type == "manager":
                    employee = Manager(employee_data["name"], employee_data["surname"], employee_data["position"], employee_data["salary"], employee_id=employee_data["employee_id"])

                else:
                    employee = Employee(employee_data["name"], employee_data["surname"], employee_data["position"], employee_data["salary"], employee_id=employee_data["employee_id"])
                employee_list.append(employee)

    return employee_list

def save_departments(departments):

    departments_list = []

    for department in departments:
        if department.leader is None:
            leader_id = None
        else:
            leader_id = department.leader.employee_id
        department_data = {"department_name": department.name, "manager_id": department.manager.employee_id, "leader_id": leader_id}
        departments_list.append(department_data)

    with open(ORGANIZATION_FILE, "w", encoding="utf-8") as f:
        json.dump(departments_list, f, indent=4, ensure_ascii=False)

def load_departments(employees):
    if not ORGANIZATION_FILE.exists():
        departments_list = []
    else:
        with open(ORGANIZATION_FILE, "r", encoding="utf-8") as f:
            departments_data = json.load(f)
            departments_list = []

            for department_data in departments_data:
                manager = None
                leader = None
                manager_id = department_data["manager_id"]
                leader_id = department_data["leader_id"]

                for employee in employees:
                    if manager_id == employee.employee_id:
                        manager = employee
                        break

                department_name = department_data["department_name"]

                if manager is None:
                    raise ValueError(f"Department {department_name} refers to missing manager ID {manager_id}.")
                else:
                    department = Department(department_name, manager)

                if leader_id is not None:
                    for employee in employees:
                        if leader_id == employee.employee_id:
                            leader = employee
                            break

                    if leader is None:
                        raise ValueError(f"Department {department_name} refers to missing leader ID {leader_id}.")

                    if leader.employee_type != "leader" :
                        raise ValueError(f"Department {department_name} refers to employee ID {leader_id}, but this employee is not a leader.")

                    leader.add_department(department)

                departments_list.append(department)

    return departments_list
